ITEMS = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items: dict, budget: int) -> tuple[list[str], int]:
    """Greedy algorithm to select products based on budget.

    :param items: Dictionary with products
    :param budget: Budget that can be spent on products.
    :return: Tuple with selected products and total calories.
    """

    # Sort items based on the ratio of calories to cost
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    total_cost = 0
    total_calories = 0
    chosen_items = []

    for item, properties in sorted_items:
        if total_cost + properties["cost"] <= budget:
            chosen_items.append(item)
            total_cost += properties["cost"]
            total_calories += properties["calories"]

    return chosen_items, total_calories


def dynamic_programming(items, budget):
    """Dynamic programming algorithm to select products based on budget.

    :param items: Dictionary with products
    :param budget: Budget that can be spent on products.
    :return: Tuple with selected products and total calories.
    """

    names = list(items.keys())
    costs = [items[name]["cost"] for name in names]
    calories = [items[name]["calories"] for name in names]

    n = len(names)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Заповнюємо таблицю dp
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Відновлюємо вибрані елементи
    w = budget
    chosen_items = []
    total_calories = dp[n][budget]

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen_items.append(names[i - 1])
            w -= costs[i - 1]

    return chosen_items, total_calories


if __name__ == "__main__":
    budget = 100

    chosen_items, total_calories = greedy_algorithm(ITEMS, budget)
    print("Greedy algorithm:")
    print("Chosen food:", chosen_items)
    print("Total Calories:", total_calories)

    chosen_items, total_calories = dynamic_programming(ITEMS, budget)
    print("Dynamic programming algorithm:")
    print("Chosen food:", chosen_items)
    print("Total Calories:", total_calories)
