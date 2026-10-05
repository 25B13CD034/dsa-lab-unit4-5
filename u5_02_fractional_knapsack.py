def fractional_knapsack(items, capacity):
    # items: list of (name, value, weight)

    # Sort items by value per kg, highest first
    ranked = sorted(
        items,
        key=lambda item: item[1] / item[2],
        reverse=True
    )

    total_value = 0.0
    remaining = capacity

    # Select items
    for name, value, weight in ranked:
        if remaining == 0:
            break

        # Take as much as possible
        take = min(weight, remaining)

        # Calculate value gained
        gained = value * take / weight

        total_value += gained
        remaining -= take

        print(f"Take {take} kg of {name:7} -> value {gained:.1f}")

    return total_value


# Main program
items = [
    ("Gold", 60, 10),
    ("Silver", 100, 20),
    ("Bronze", 120, 30)
]

best = fractional_knapsack(items, 50)

print("Best value:", best)