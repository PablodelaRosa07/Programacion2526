import random
import tkinter as tk
from tkinter import messagebox

CARD_VALUES = '23456789TJQKA'
SUITS = '♠♥♦♣'
CARD_ORDER = {k: i for i, k in enumerate(CARD_VALUES, 2)}

def create_deck():
    return [v + s for v in CARD_VALUES for s in SUITS]

def deal_cards(deck, num):
    return [deck.pop() for _ in range(num)]

def hand_name(rank):
    names = {
        10: "Escalera Real",
        9: "Escalera de Color",
        8: "Poker",
        7: "Full House",
        6: "Color",
        5: "Escalera",
        4: "Trío",
        3: "Doble Pareja",
        2: "Pareja",
        1: "Carta Alta"
    }
    return names[rank]

from collections import Counter

def get_hand_rank(cards):
    values = sorted([c[0] for c in cards], key=lambda x: CARD_ORDER[x], reverse=True)
    suits = [c[1] for c in cards]

    val_counts = Counter(values)
    counts = sorted(val_counts.values(), reverse=True)
    sorted_vals = sorted(val_counts.items(), key=lambda x: (-x[1], -CARD_ORDER[x[0]]))
    ordered_vals = [v for v, count in sorted_vals]

    flush = False
    straight = False
    straight_high = None

    suit_counts = Counter(suits)
    flush_suit = None
    for suit, count in suit_counts.items():
        if count >= 5:
            flush = True
            flush_suit = suit
            break

    unique_vals = sorted(set(values), key=lambda x: CARD_ORDER[x], reverse=True)
    for i in range(len(unique_vals) - 4 + 1):
        slice_vals = unique_vals[i:i + 5]
        if all(CARD_ORDER[slice_vals[j]] - 1 == CARD_ORDER[slice_vals[j + 1]] for j in range(4)):
            straight = True
            straight_high = slice_vals[0]
            break

    if set('A2345').issubset(set(values)):
        straight = True
        straight_high = '5'

    if flush:
        flush_cards = [c for c in cards if c[1] == flush_suit]
        flush_vals = sorted([c[0] for c in flush_cards], key=lambda x: CARD_ORDER[x], reverse=True)
        unique_flush_vals = sorted(set(flush_vals), key=lambda x: CARD_ORDER[x], reverse=True)
        for i in range(len(unique_flush_vals) - 4 + 1):
            slice_vals = unique_flush_vals[i:i + 5]
            if all(CARD_ORDER[slice_vals[j]] - 1 == CARD_ORDER[slice_vals[j + 1]] for j in range(4)):
                if slice_vals[0] == 'A':
                    return (10, ['A'])
                return (9, [slice_vals[0]])

    if counts[0] == 4:
        return (8, [ordered_vals[0], ordered_vals[1]])

    if counts[0] == 3 and counts[1] >= 2:
        return (7, [ordered_vals[0], ordered_vals[1]])

    if flush:
        top_flush_cards = [c for c in cards if c[1] == flush_suit]
        top_flush_vals = sorted([c[0] for c in top_flush_cards], key=lambda x: CARD_ORDER[x], reverse=True)
        return (6, top_flush_vals[:5])

    if straight:
        return (5, [straight_high])

    if counts[0] == 3:
        return (4, [ordered_vals[0]] + ordered_vals[1:3])

    if counts[0] == 2 and counts[1] == 2:
        return (3, [ordered_vals[0], ordered_vals[1], ordered_vals[2]])

    if counts[0] == 2:
        return (2, [ordered_vals[0]] + ordered_vals[1:4])

    return (1, ordered_vals[:5])

def compare_hands(player_best, cpu_best):
    if player_best[0] > cpu_best[0]:
        return "Jugador gana con " + hand_name(player_best[0])
    elif player_best[0] < cpu_best[0]:
        return "CPU gana con " + hand_name(cpu_best[0])
    else:
        for pv, cv in zip(player_best[1], cpu_best[1]):
            if CARD_ORDER[pv] > CARD_ORDER[cv]:
                return "Jugador gana con " + hand_name(player_best[0]) + " (desempate)"
            elif CARD_ORDER[pv] < CARD_ORDER[cv]:
                return "CPU gana con " + hand_name(cpu_best[0]) + " (desempate)"
        return "Empate"

class PokerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Poker Texas Hold'em Interactivo")

        self.deck = []
        self.player_cards = []
        self.cpu_cards = []
        self.community_cards = []

        self.labels = []

        self.status_label = tk.Label(root, text="Presiona 'Comenzar' para iniciar el juego.", font=("Arial", 12))
        self.status_label.pack(pady=10)

        self.card_frame = tk.Frame(root)
        self.card_frame.pack()

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.start_button = tk.Button(self.button_frame, text="Comenzar", command=self.start_game)
        self.start_button.grid(row=0, column=0, padx=5)

        self.next_stage_button = tk.Button(self.button_frame, text="Siguiente etapa", command=self.next_stage, state=tk.DISABLED)
        self.next_stage_button.grid(row=0, column=1, padx=5)

        self.fold_button = tk.Button(self.button_frame, text="Retirarse (Fold)", command=self.fold, state=tk.DISABLED)
        self.fold_button.grid(row=0, column=2, padx=5)

        self.bet_button = tk.Button(self.button_frame, text="Apostar", command=self.bet, state=tk.DISABLED)
        self.bet_button.grid(row=0, column=3, padx=5)

        self.stage = 0  # 0=pre-flop, 1=flop, 2=turn, 3=river, 4=resultado

    def clear_cards(self):
        for label in self.labels:
            label.destroy()
        self.labels = []

    def show_cards(self, label, cards):
        row = tk.Frame(self.card_frame)
        tk.Label(row, text=label + ": ", font=("Arial", 12, "bold")).pack(side="left")
        for card in cards:
            card_lbl = tk.Label(row, text=card, font=("Courier", 16), borderwidth=2, relief="groove", width=4)
            card_lbl.pack(side="left", padx=2)
            self.labels.append(card_lbl)
        row.pack(pady=2)

    def start_game(self):
        self.clear_cards()
        self.deck = create_deck()
        random.shuffle(self.deck)

        self.player_cards = deal_cards(self.deck, 2)
        self.cpu_cards = deal_cards(self.deck, 2)
        self.community_cards = []

        self.stage = 0

        self.status_label.config(text="Manos repartidas. Es tu turno: puedes apostar o retirarte.")
        self.show_cards("Jugador", self.player_cards)
        self.show_cards("CPU", ['??', '??'])

        self.start_button.config(state=tk.DISABLED)
        self.next_stage_button.config(state=tk.DISABLED)
        self.fold_button.config(state=tk.NORMAL)
        self.bet_button.config(state=tk.NORMAL)

    def next_stage(self):
        self.clear_cards()
        if self.stage == 0:  # Flop
            self.community_cards += deal_cards(self.deck, 3)
            self.status_label.config(text="Flop repartido. Decide tu acción.")
            self.stage = 1
        elif self.stage == 1:  # Turn
            self.community_cards += deal_cards(self.deck, 1)
            self.status_label.config(text="Turn repartido. Decide tu acción.")
            self.stage = 2
        elif self.stage == 2:  # River
            self.community_cards += deal_cards(self.deck, 1)
            self.status_label.config(text="River repartido. Decide tu acción.")
            self.stage = 3
        elif self.stage == 3:  # Resultado
            self.status_label.config(text="Evaluando manos...")
            self.stage = 4
            self.show_result()
            return

        self.show_cards("Jugador", self.player_cards)
        self.show_cards("CPU", ['??', '??'])
        self.show_cards("Comunitarias", self.community_cards)

        self.fold_button.config(state=tk.NORMAL)
        self.bet_button.config(state=tk.NORMAL)
        self.next_stage_button.config(state=tk.DISABLED)

    def fold(self):
        self.status_label.config(text="Jugador se retiró. ¡Gana CPU!")
        self.show_cards("Jugador", self.player_cards)
        self.show_cards("CPU", self.cpu_cards)
        self.show_cards("Comunitarias", self.community_cards)
        self.fold_button.config(state=tk.DISABLED)
        self.bet_button.config(state=tk.DISABLED)
        self.next_stage_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.NORMAL)

    def bet(self):
        # Aquí podrías agregar lógica de apuestas
        # Por ahora simplemente avanza la ronda
        self.status_label.config(text="Has apostado. Repartiendo siguiente etapa...")
        self.fold_button.config(state=tk.DISABLED)
        self.bet_button.config(state=tk.DISABLED)
        self.next_stage_button.config(state=tk.NORMAL)

    def show_result(self):
        self.clear_cards()
        self.show_cards("Jugador", self.player_cards)
        self.show_cards("CPU", self.cpu_cards)
        self.show_cards("Comunitarias", self.community_cards)

        player_best = get_hand_rank(self.player_cards + self.community_cards)
        cpu_best = get_hand_rank(self.cpu_cards + self.community_cards)

        result = compare_hands(player_best, cpu_best)
        self.status_label.config(text="🏆 Resultado: " + result)

        self.start_button.config(state=tk.NORMAL)
        self.next_stage_button.config(state=tk.DISABLED)
        self.fold_button.config(state=tk.DISABLED)
        self.bet_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    gui = PokerGUI(root)
    root.mainloop()
