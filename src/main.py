import numpy as np
import matplotlib.pyplot as plt


def fitness_function(x):
    return x * np.sin(10 * np.pi * x) + np.cos(5 * np.pi * x) ** 6


def initialize_population(size):
    return np.random.rand(size)


def select(population, fitness, num_parents):
    parents = np.empty(num_parents)
    fitness_copy = fitness.copy()
    for i in range(num_parents):
        max_index = np.argmax(fitness_copy)
        parents[i] = population[max_index]
        fitness_copy[max_index] = -np.inf
    return parents


def crossover(parents, num_offspring):
    offspring = np.empty(num_offspring)
    for k in range(num_offspring):
        parent1_idx = k % parents.size
        parent2_idx = (k + 1) % parents.size
        offspring[k] = (parents[parent1_idx] + parents[parent2_idx]) / 2
    return offspring


def mutation(offspring):
    for idx in range(offspring.size):
        random_change = np.random.uniform(-0.1, 0.1)
        offspring[idx] += random_change
    return offspring


def genetic_algorithm(population_size, num_generations, num_parents_mating):
    population = initialize_population(population_size)
    for generation in range(num_generations):
        fitness = fitness_function(population)
        parents = select(population, fitness, num_parents_mating)
        offspring = crossover(parents, population_size - parents.size)
        offspring = mutation(offspring)
        population[: parents.size] = parents
        population[parents.size :] = offspring

    final_fitness = fitness_function(population)
    best_match_idx = np.argmax(final_fitness)
    return population[best_match_idx], final_fitness[best_match_idx]


def plot_function(best_solution, best_solution_fitness):
    x_values = np.linspace(0, 1, 400)
    y_values = fitness_function(x_values)
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label="f(x) = x * sin(10πx) + cos(5πx)^6")
    plt.scatter(best_solution, best_solution_fitness, color="red", label="Best Solution")
    plt.title("Function Plot")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    population_size = 50
    num_generations = 40
    num_parents_mating = 25

    best_solution, best_solution_fitness = genetic_algorithm(
        population_size, num_generations, num_parents_mating
    )
    print("Best Solution: x =", best_solution)
    print("Fitness of Best Solution:", best_solution_fitness)

    plot_function(best_solution, best_solution_fitness)
