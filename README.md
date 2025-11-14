Genetic Algorithm Optimizer (Python)

A small Python project that uses a genetic algorithm to search for the global maximum of a nonlinear function:
f(x) = x * sin(10πx) + cos^6(5πx).

The script initialises a population of candidate solutions in [0, 1], evaluates fitness with the objective function, and then uses selection, crossover and mutation to evolve the population for a fixed number of generations. The best solution and its fitness are printed at the end.

The program can also plot the objective function on [0, 1] and mark the best solution found, so the behaviour of the algorithm is easy to see.

Project Structure

ga-optimizer-python/
  src/
    main.py
  README.md

How to Run

From the ga-optimizer-python folder:

python src/main.py
