import tkinter as tk
from tkinter import messagebox
import os

# Configuración básica
BLOCK_SIZE = 32
VISIBLE_WIDTH = 20
VISIBLE_HEIGHT = 15

WORLD_WIDTH = 60
WORLD_HEIGHT = 20

GRAVITY_DELAY = 100

BLOCKS = {
    "air": None,
    "grass": "green",
    "dirt": "saddle brown",
    "stone": "gray",
    "water": "blue",
    "sand": "khaki",
    "wood": "sienna",
    "leaves": "forest green",
    "enemy": "lime green",  # No es bloque, solo para visual enemigo
}

SOLID_BLOCKS = {"grass", "dirt", "stone", "sand", "wood", "leaves"}

world = [["air" for _ in range(WORLD_WIDTH)] for _ in range(WORLD_HEIGHT)]

for x in range(WORLD_WIDTH):
    world[WORLD_HEIGHT-1][x] = "grass"
    world[WORLD_HEIGHT-2][x] = "dirt"
    if x % 7 == 0:
        world[WORLD_HEIGHT-3][x] = "stone"

player_x, player_y = 5.0, WORLD_HEIGHT - 4.0
player_vy = 0.0
on_ground = False
player_life = 5

camera_x = 0
camera_y = WORLD_HEIGHT - VISIBLE_HEIGHT
if camera_y < 0:
    camera_y = 0

current_block = "grass"

SAVE_FILE = "miniminecraft_world.txt"

inventory = {}

CRAFTING_RECIPES = {
    "wood": {"dirt": 2, "stone": 1},
    "stone": {"dirt": 3},
    "sand": {"dirt": 2, "stone": 1},
}

def save_world():
    try:
        with open(SAVE_FILE, "w") as f:
            for row in world:
                f.write(",".join(row) + "\n")
        messagebox.showinfo("Guardar", "Mundo guardado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar el mundo:\n{e}")

def load_world():
    global world
    if not os.path.exists(SAVE_FILE):
        messagebox.showinfo("Cargar", "No existe un mundo guardado aún.")
        return
    try:
        with open(SAVE_FILE, "r") as f:
            lines = f.readlines()
        new_world = []
        for line in lines:
            blocks = line.strip().split(",")
            new_world.append(blocks)
        if len(new_world) == WORLD_HEIGHT and all(len(r) == WORLD_WIDTH for r in new_world):
            world[:] = new_world
            messagebox.showinfo("Cargar", "Mundo cargado correctamente.")
        else:
            messagebox.showerror("Error", "El archivo guardado no es compatible.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar el mundo:\n{e}")

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0.05  # velocidad horizontal

    def update(self):
        new_x = self.x + self.dx
        if new_x < 0 or new_x >= WORLD_WIDTH - 1:
            self.dx = -self.dx
            return
        if is_solid(new_x, self.y) or is_solid(new_x + 0.9, self.y):
            self.dx = -self.dx
        else:
            self.x = new_x

    def draw(self, canvas, cam_x, cam_y):
        px = (self.x - cam_x) * BLOCK_SIZE
        py = (self.y - cam_y) * BLOCK_SIZE
        canvas.create_rectangle(px, py, px + BLOCK_SIZE, py + BLOCK_SIZE, fill=BLOCKS["enemy"], outline="black")

enemies = [
    Enemy(15, WORLD_HEIGHT - 4),
    Enemy(30, WORLD_HEIGHT - 4),
    Enemy(45, WORLD_HEIGHT - 4),
]

def add_to_inventory(block):
    if block == "air":
        return
    inventory[block] = inventory.get(block, 0) + 1

def remove_from_inventory(block, amount=1):
    if block in inventory and inventory[block] >= amount:
        inventory[block] -= amount
        if inventory[block] == 0:
            del inventory[block]
        return True
    return False

def open_crafting_menu():
    crafting_window = tk.Toplevel(root)
    crafting_window.title("Crafting")

    tk.Label(crafting_window, text="Inventario:").grid(row=0, column=0, columnspan=2)
    row_idx = 1
    for blk, qty in inventory.items():
        tk.Label(crafting_window, text=f"{blk}: {qty}").grid(row=row_idx, column=0)
        row_idx += 1

    tk.Label(crafting_window, text="Recetas:").grid(row=0, column=2, columnspan=2)
    row_idx = 1
    for product, recipe in CRAFTING_RECIPES.items():
        reqs = ", ".join(f"{k}x{v}" for k, v in recipe.items())
        btn = tk.Button(crafting_window, text=f"{product} ({reqs})",
                        command=lambda p=product: try_craft(p, crafting_window))
        btn.grid(row=row_idx, column=2, columnspan=2, sticky="ew", padx=5, pady=2)
        row_idx += 1

def try_craft(product, win):
    recipe = CRAFTING_RECIPES[product]
    for mat, amt in recipe.items():
        if inventory.get(mat, 0) < amt:
            messagebox.showinfo("Crafting", f"No tienes suficientes {mat}")
            return
    for mat, amt in recipe.items():
        remove_from_inventory(mat, amt)
    inventory[product] = inventory.get(product, 0) + 1
    messagebox.showinfo("Crafting", f"Has creado 1 {product}")
    win.destroy()

def draw_world():
    canvas.delete("all")
    for y in range(VISIBLE_HEIGHT):
        for x in range(VISIBLE_WIDTH):
            wx = camera_x + x
            wy = camera_y + y
            if wx >= WORLD_WIDTH or wy >= WORLD_HEIGHT:
                continue
            block = world[wy][wx]
            color = BLOCKS.get(block)
            if color:
                canvas.create_rectangle(
                    x*BLOCK_SIZE, y*BLOCK_SIZE,
                    (x+1)*BLOCK_SIZE, (y+1)*BLOCK_SIZE,
                    fill=color, outline="black"
                )
    for enemy in enemies:
        enemy.draw(canvas, camera_x, camera_y)

    px = (player_x - camera_x) * BLOCK_SIZE
    py = (player_y - camera_y) * BLOCK_SIZE
    canvas.create_rectangle(px, py, px + BLOCK_SIZE, py + BLOCK_SIZE, fill="red", outline="black")

    canvas.create_text(10, 10, anchor="nw", text=f"Bloque: {current_block}", font=("Arial", 14), fill="white")
    inv_text = "Inventario: " + ", ".join(f"{k}x{v}" for k, v in inventory.items())
    canvas.create_text(10, 30, anchor="nw", text=inv_text, font=("Arial", 12), fill="white")
    canvas.create_text(10, 50, anchor="nw", text=f"Vida: {player_life}", font=("Arial", 12), fill="white")

def is_solid(x, y):
    if 0 <= x < WORLD_WIDTH and 0 <= y < WORLD_HEIGHT:
        return world[int(y)][int(x)] in SOLID_BLOCKS
    return False

def update_player():
    global player_x, player_y, player_vy, on_ground, camera_x, camera_y, player_life

    speed = 0.1
    if keys_pressed["left"]:
        new_x = player_x - speed
        if not is_solid(new_x, player_y):
            player_x = max(0, new_x)
    if keys_pressed["right"]:
        new_x = player_x + speed
        if not is_solid(new_x + 0.99, player_y):
            player_x = min(WORLD_WIDTH - 1, new_x)

    player_vy += 0.02
    new_y = player_y + player_vy

    if player_vy > 0:
        if is_solid(player_x, new_y + 0.99) or is_solid(player_x + 0.99, new_y + 0.99):
            player_y = int(new_y + 0.99) - 1
            player_vy = 0
            on_ground = True
        else:
            player_y = new_y
            on_ground = False
    elif player_vy < 0:
        if is_solid(player_x, new_y) or is_solid(player_x + 0.99, new_y):
            player_vy = 0
        else:
            player_y = new_y

    for enemy in enemies:
        if (int(player_x) == int(enemy.x) and int(player_y) == int(enemy.y)):
            player_life -= 1
            if keys_pressed["left"]:
                player_x += 1
            elif keys_pressed["right"]:
                player_x -= 1
            if player_life <= 0:
                messagebox.showinfo("Juego terminado", "Has perdido toda tu vida!")
                root.quit()

    for enemy in enemies:
        enemy.update()

    target_camera_x = int(player_x) - VISIBLE_WIDTH // 2
    camera_x = max(0, min(WORLD_WIDTH - VISIBLE_WIDTH, target_camera_x))

    target_camera_y = WORLD_HEIGHT - VISIBLE_HEIGHT
    if target_camera_y < 0:
        target_camera_y = 0
    camera_y = target_camera_y

def on_key_press(event):
    key = event.keysym.lower()
    if key in keys_pressed:
        keys_pressed[key] = True
    if key == "space":
        global player_vy, on_ground
        if on_ground:
            player_vy = -0.5
            on_ground = False
    if key == "1":
        set_current_block("grass")
    elif key == "2":
        set_current_block("dirt")
    elif key == "3":
        set_current_block("stone")
    elif key == "4":
        set_current_block("wood")
    elif key == "5":
        set_current_block("leaves")
    elif key == "c":
        open_crafting_menu()
    elif key == "s":
        save_world()
    elif key == "l":
        load_world()

def on_key_release(event):
    key = event.keysym.lower()
    if key in keys_pressed:
        keys_pressed[key] = False

def set_current_block(block):
    global current_block
    if block in BLOCKS:
        current_block = block

def on_mouse_click(event):
    x = event.x // BLOCK_SIZE + camera_x
    y = event.y // BLOCK_SIZE + camera_y
    if 0 <= x < WORLD_WIDTH and 0 <= y < WORLD_HEIGHT:
        if event.num == 1:  # Click izquierdo: colocar bloque
            below = y + 1
            if below < WORLD_HEIGHT and is_solid(x, below):
                if inventory.get(current_block, 0) > 0:
                    world[y][x] = current_block
                    remove_from_inventory(current_block)
        elif event.num == 3:  # Click derecho: destruir bloque
            block = world[y][x]
            if block != "air":
                add_to_inventory(block)
                world[y][x] = "air"

def game_loop():
    update_player()
    draw_world()
    root.after(GRAVITY_DELAY, game_loop)

root = tk.Tk()
root.title("Mini Minecraft")

canvas = tk.Canvas(root, width=VISIBLE_WIDTH*BLOCK_SIZE, height=VISIBLE_HEIGHT*BLOCK_SIZE, bg="black")
canvas.pack()

keys_pressed = {"left": False, "right": False}

root.bind("<KeyPress>", on_key_press)
root.bind("<KeyRelease>", on_key_release)
canvas.bind("<Button-1>", on_mouse_click)
canvas.bind("<Button-3>", on_mouse_click)

game_loop()
root.mainloop()
