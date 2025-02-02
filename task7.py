import random
import matplotlib.pyplot as plt
import pandas as pd

ANALYTICAL_PROBABILITIES = {
    2: 2.78,  # 1/36
    3: 5.56,  # 2/36
    4: 8.33,  # 3/36
    5: 11.11,  # 4/36
    6: 13.89,  # 5/36
    7: 16.67,  # 6/36
    8: 13.89,  # 5/36
    9: 11.11,  # 4/36
    10: 8.33,  # 3/36
    11: 5.56,  # 2/36
    12: 2.78,  # 1/36
}


def monte_carlo_simulation(num_simulations: int) -> dict[int, float]:
    """Simulate rolling two dice and calculate the probability of each sum.

    :param num_simulations: The number of simulations to run.
    :return: A dictionary with the sum of the dice as keys and the probability as values.
    """
    sum_counts = {i: 0 for i in range(2, 12 + 1)}

    for _ in range(num_simulations):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        sum_counts[dice_sum] += 1

    probabilities = {sum_val: count / num_simulations * 100 for sum_val, count in sum_counts.items()}
    return probabilities


if __name__ == "__main__":

    num_simulations = 100000
    simulated_probabilities = monte_carlo_simulation(num_simulations)

    # Compare analytical and simulated probabilities
    sums = list(ANALYTICAL_PROBABILITIES.keys())
    analytical_values = list(ANALYTICAL_PROBABILITIES.values())
    simulated_values = [simulated_probabilities[sum_val] for sum_val in sums]

    # Build a plot
    plt.figure(figsize=(10, 6))
    plt.plot(sums, analytical_values, marker="o", linestyle="-", label="Analytical Probabilities")
    plt.plot(sums, simulated_values, marker="x", linestyle="--", label="Monte Carlo Simulated Probabilities")
    plt.xlabel("Sum of Two Dice")
    plt.ylabel("Probability (%)")
    plt.title("Comparison of Analytical and Monte Carlo Simulated Probabilities")
    plt.legend()
    plt.grid(True)
    plt.show()
    table_data = {
        "Sum": sums,
        "Analytical (%)": analytical_values,
        "Monte Carlo (%)": simulated_values,
    }
    df = pd.DataFrame(table_data)
    print(df)
