import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


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
    fig, ax = plt.subplots(figsize=(12, 6))
    for path in results:
        ax.plot(path, alpha=0.7)

    ax.axhline(y=0, color='red', linestyle='--', label='Bankrupt')
    ax.set_title(f'Monte Carlo Simulation of Blackjack Bankrolls ({num_hands} Hands)')
    ax.set_xlabel('Number of Hands Played')
    ax.set_ylabel('Bankroll ($)')
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)


# Streamlit UI
st.title("Blackjack Monte Carlo Simulator")

initial_bankroll = st.number_input("Initial Bankroll ($):", min_value=1, value=150)
bet_size = st.number_input("Bet Size ($):", min_value=1, value=15)
house_edge_percent = st.number_input("House Edge (%):", value=-0.5, step=0.1)
house_edge = house_edge_percent / 100
num_hands = st.number_input("Number of Hands:", min_value=1, value=400)
num_paths = st.number_input("Number of Simulated Players:", min_value=1, value=20)

if st.button("Run Simulation"):
    blackjack_monte_carlo(
        initial_bankroll=initial_bankroll,
        bet_size=bet_size,
        house_edge=house_edge,
        num_hands=num_hands,
        num_paths=num_paths
    )
