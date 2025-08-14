## Implement a program to minimize the Sphere function using three different local optimization approaches:

- Hill Climbing Algorithm

- Random Local Search

- Simulated Annealing

## Technical Requirements

Iterations parameter:
Each algorithm must accept a parameter iterations that determines the maximum number of iterations.

Stopping conditions:

- If the change in the objective function value or the point's position in the search space between two consecutive iterations is less than epsilon, the algorithm stops (where epsilon is the accuracy parameter).

- For the Simulated Annealing algorithm, temperature is also considered: if the temperature decreases below epsilon, the algorithm stops, as this indicates the search capability is exhausted.

