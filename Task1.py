import random
import math


# Definition of the Sphere function
def sphere_function(x):
    return sum(xi ** 2 for xi in x)


# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    dimensions = len(bounds)
    current_solution = [random.uniform(*b) for b in bounds]
    current_value = func(current_solution)

    for _ in range(iterations):
        # Generate a neighboring point
        neighbor = [
            max(
                min(current_solution[i] + random.uniform(-0.1, 0.1), bounds[i][1]),
                bounds[i][0],
            )
            for i in range(dimensions)
        ]
        neighbor_value = func(neighbor)

        # Update if a better value is found
        if neighbor_value < current_value:
            current_solution, current_value = neighbor, neighbor_value

        # Check for epsilon convergence
        if abs(neighbor_value - current_value) < epsilon:
            break

    return current_solution, current_value


# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    best_solution = [random.uniform(*b) for b in bounds]
    best_value = func(best_solution)

    for _ in range(iterations):
        candidate = [random.uniform(*b) for b in bounds]
        candidate_value = func(candidate)

        if candidate_value < best_value:
            best_solution, best_value = candidate, candidate_value

        if abs(candidate_value - best_value) < epsilon:
            break

    return best_solution, best_value


# Simulated Annealing
def simulated_annealing(
        func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6
):
    dimensions = len(bounds)
    current_solution = [random.uniform(*b) for b in bounds]
    current_value = func(current_solution)
    best_solution, best_value = current_solution, current_value

    for _ in range(iterations):
        # Generate a neighboring point
        neighbor = [
            max(
                min(current_solution[i] + random.uniform(-0.1, 0.1), bounds[i][1]),
                bounds[i][0],
            )
            for i in range(dimensions)
        ]
        neighbor_value = func(neighbor)

        # Accept new point according to Metropolis criterion
        if neighbor_value < current_value or random.random() < math.exp(
                (current_value - neighbor_value) / temp
        ):
            current_solution, current_value = neighbor, neighbor_value

        # Update the best found solution
        if current_value < best_value:
            best_solution, best_value = current_solution, current_value

        # Reduce temperature
        temp *= cooling_rate

        if temp < epsilon:
            break

    return best_solution, best_value


if __name__ == "__main__":
    # Bounds for the function
    bounds = [(-5, 5), (-5, 5)]

    # Run the algorithms
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Solution:", hc_solution, "Value:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Solution:", rls_solution, "Value:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Solution:", sa_solution, "Value:", sa_value)
