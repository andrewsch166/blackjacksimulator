import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk


def blackjack_monte_carlo(
    initial_bankroll=150,
    bet_size=15,
    house_edge=-0.005,
    std_dev_per_hand=None,
    num_hands=400,
    num_paths=20
):
    if std_dev_per_hand is None:
        std_dev_per_hand = 1.14 * bet_size

    results = []

    for _ in range(num_paths):
        bankroll = [initial_bankroll]
        for _ in range(num_hands):
            if bankroll[-1] <= 0:
                bankroll.append(0)
            else:
                outcome = np.random.normal(loc=house_edge * bet_size, scale=std_dev_per_hand)
                bankroll.append(max(0, bankroll[-1] + outcome))
        results.append(bankroll)

    # Plotting the results
    plt.figure(figsize=(12, 6))
    for path in results:
        plt.plot(path, alpha=0.7)

    plt.axhline(y=0, color='red', linestyle='--', label='Bankrupt')
    plt.title(f'Monte Carlo Simulation of Blackjack Bankrolls ({num_hands} Hands)')
    plt.xlabel('Number of Hands Played')
    plt.ylabel('Bankroll ($)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


def run_gui():
    def simulate():
        bankroll = float(bankroll_var.get())
        bet = float(bet_var.get())
        edge = float(edge_var.get()) / 100
        hands = int(hands_var.get())
        paths = int(paths_var.get())
        blackjack_monte_carlo(
            initial_bankroll=bankroll,
            bet_size=bet,
            house_edge=edge,
            num_hands=hands,
            num_paths=paths
        )

    root = tk.Tk()
    root.title("Blackjack Monte Carlo Simulator")

    # Input frame
    frame = ttk.Frame(root, padding=10)
    frame.grid(row=0, column=0, sticky="EW")

    ttk.Label(frame, text="Initial Bankroll ($):").grid(row=0, column=0, sticky="W")
    bankroll_var = tk.StringVar(value="150")
    ttk.Entry(frame, textvariable=bankroll_var).grid(row=0, column=1)

    ttk.Label(frame, text="Bet Size ($):").grid(row=1, column=0, sticky="W")
    bet_var = tk.StringVar(value="15")
    ttk.Entry(frame, textvariable=bet_var).grid(row=1, column=1)

    ttk.Label(frame, text="House Edge (%):").grid(row=2, column=0, sticky="W")
    edge_var = tk.StringVar(value="-0.5")
    ttk.Entry(frame, textvariable=edge_var).grid(row=2, column=1)

    ttk.Label(frame, text="Number of Hands:").grid(row=3, column=0, sticky="W")
    hands_var = tk.StringVar(value="400")
    ttk.Entry(frame, textvariable=hands_var).grid(row=3, column=1)

    ttk.Label(frame, text="Number of Paths:").grid(row=4, column=0, sticky="W")
    paths_var = tk.StringVar(value="20")
    ttk.Entry(frame, textvariable=paths_var).grid(row=4, column=1)

    ttk.Button(frame, text="Run Simulation", command=simulate).grid(row=5, column=0, columnspan=2, pady=10)

    root.mainloop()


if __name__ == "__main__":
    run_gui()
