# Project Title

## Description

This project implements a depth-first search (DFS) algorithm for the knapsack problem. The algorithm explores two possibilities for each item: including the item and excluding the item. It then returns the maximum value obtained from these two possibilities.

## Project Structure

- `genetique.py`: This file contains the implementation of the genetic algorithm.
- `RecuitSimule.py`: This file contains the implementation of the simulated annealing algorithm.
- `data.csv`: This file contains the data for the knapsack problem.
- `README.md`: This file contains the documentation for the project.

## Usage

To use this project, call the `knapsack_dfs` function with a given capacity. The function will return the maximum value and the list of selected items.

## Complexity

The time complexity of the DFS algorithm depends on the number of items and the capacity of the knapsack. In the worst case, the DFS algorithm explores all possible combinations, resulting in an exponential time complexity of O(2^n), where n is the number of items.

The space complexity depends on the maximum depth of the recursive call stack, which is also exponential in the worst case.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
