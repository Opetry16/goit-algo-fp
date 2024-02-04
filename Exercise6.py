def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0

    for item_name, item_info in sorted_items:
        if total_cost + item_info['cost'] <= budget:
            selected_items.append(item_name)
            total_cost += item_info['cost']
            total_calories += item_info['calories']

    return {'selected_items': selected_items, 'total_cost': total_cost, 'total_calories': total_calories}

def dynamic_programming(items, budget):
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            cost = items[list(items.keys())[i-1]]['cost']
            calories = items[list(items.keys())[i-1]]['calories']

            if cost <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-cost] + calories)
            else:
                dp[i][w] = dp[i-1][w]

    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(list(items.keys())[i-1])
            w -= items[list(items.keys())[i-1]]['cost']

    selected_items.reverse()

    return {'selected_items': selected_items, 'total_cost': dp[n][budget], 'total_calories': dp[n][budget]}

# Задані дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Бюджет
budget = 100

# Жадібний алгоритм
greedy_result = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Обрані страви:", greedy_result['selected_items'])
print("Загальна вартість:", greedy_result['total_cost'])
print("Загальна калорійність:", greedy_result['total_calories'])
print()

# Алгоритм динамічного програмування
dp_result = dynamic_programming(items, budget)
print("Алгоритм динамічного програмування:")
print("Обрані страви:", dp_result['selected_items'])
print("Загальна вартість:", dp_result['total_cost'])
print("Загальна калорійність:", dp_result['total_calories'])
