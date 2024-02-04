import random
import matplotlib.pyplot as plt
import numpy as np

def monte_carlo_simulation(num_trials):
    results = {i: 0 for i in range(2, 13)}

    for _ in range(num_trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        results[total] += 1

    probabilities = {k: v / num_trials * 100 for k, v in results.items()}
    return probabilities

def analytical_probabilities():
    probabilities = {2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
                     8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36}
    return probabilities

def plot_probabilities(monte_carlo_prob, analytical_prob):
    labels = [str(i) for i in range(2, 13)]
    monte_carlo_values = [monte_carlo_prob[i] for i in range(2, 13)]
    analytical_values = [analytical_prob[i] * 100 for i in range(2, 13)]

    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, monte_carlo_values, width, label='Monte Carlo')
    rects2 = ax.bar(x + width/2, analytical_values, width, label='Analytical')

    ax.set_xlabel('Sum')
    ax.set_ylabel('Probability (%)')
    ax.set_title('Probabilities of Dice Sums')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    plt.show()

# Кількість імітацій
num_trials = 100000

# Запуск імітації та отримання ймовірностей за допомогою методу Монте-Карло
monte_carlo_probabilities = monte_carlo_simulation(num_trials)

# Отримання аналітичних ймовірностей
analytical_probabilities = analytical_probabilities()

# Виведення результатів та порівняння
print("Monte Carlo Probabilities:")
for k, v in monte_carlo_probabilities.items():
    print(f"Sum {k}: {v:.2f}%")

print("\nAnalytical Probabilities:")
for k, v in analytical_probabilities.items():
    print(f"Sum {k}: {v*100:.2f}%")

# Графічне відображення порівняння
plot_probabilities(monte_carlo_probabilities, analytical_probabilities)
