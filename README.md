## AI CIA

# CIA-1 AI Search Algorithm Implementations

This repository contains implementations of various algorithms commonly used in search and optimization problems. Each algorithm is described below, along with its purpose and key characteristics.

## Table of Contents
1. [British Museum Search](#british-museum-search)
2. [Depth-First Search (DFS)](#depth-first-search-dfs)
3. [Breadth-First Search (BFS)](#breadth-first-search-bfs)
4. [Hill Climbing](#hill-climbing)
5. [Beam Search](#beam-search)
6. [Oracle](#oracle)
7. [Branch and Bound (B&B)](#branch-and-bound-bb)
8. [Branch & Bound Greedy](#branch--bound-greedy)
9. [Branch & Bound Greedy with Exit](#branch--bound-greedy-with-exit)
10. [Branch & Bound Greedy with Heuristic](#branch--bound-greedy-with-heuristic)
11. [Branch & Bound Heuristic](#branch--bound-heuristic)
12. [A* Algorithm](#a-algorithm)

## Algorithms

### British Museum Search
- **Description**: A search algorithm inspired by the British Museum, focusing on optimizing the search for items within a vast dataset.
- **Use Cases**: Suitable for scenarios where structured search within a large dataset is required.

### Depth-First Search (DFS)
- **Description**: A traversal algorithm that explores as far as possible along each branch before backtracking.
- **Complexity**: O(V + E) where V is the number of vertices and E is the number of edges.
- **Use Cases**: Useful for pathfinding, topological sorting, and solving puzzles.

### Breadth-First Search (BFS)
- **Description**: A traversal algorithm that explores all neighbors at the present depth prior to moving on to nodes at the next depth level.
- **Complexity**: O(V + E).
- **Use Cases**: Finding the shortest path in unweighted graphs and level-order traversal of trees.

### Hill Climbing
- **Description**: An optimization algorithm that continuously moves towards increasing value (uphill) until no higher value can be found.
- **Use Cases**: Used in mathematical optimization problems, artificial intelligence, and game development.

### Beam Search
- **Description**: A search algorithm that explores a graph by expanding the most promising nodes, keeping a limited number of paths (the beam width).
- **Use Cases**: Often used in natural language processing and AI.

### Oracle
- **Description**: An algorithm that leverages a "black box" for obtaining solutions, often used in theoretical computer science.
- **Use Cases**: Analyzing decision-making processes and optimizing queries.

### Branch and Bound (B&B)
- **Description**: An optimization technique that divides the problem into smaller subproblems and systematically explores branches to find the optimal solution.
- **Use Cases**: Solving combinatorial optimization problems.

### Branch & Bound Greedy
- **Description**: A variant of the B&B algorithm that employs a greedy approach to make local optimal choices.
- **Use Cases**: Used in optimization problems where a quick, good-enough solution is acceptable.

### Branch & Bound Greedy with Exit
- **Description**: An extension of the greedy approach that allows for early exits from the search if a satisfactory solution is found.
- **Use Cases**: Applicable in real-time systems where time constraints are critical.

### Branch & Bound Greedy with Heuristic
- **Description**: Combines the greedy approach with heuristics to guide the search process.
- **Use Cases**: Useful in scenarios where heuristics can significantly reduce the search space.

### Branch & Bound Heuristic
- **Description**: An approach that uses heuristics to determine the most promising nodes to explore in the B&B algorithm.
- **Use Cases**: Enhancing the efficiency of traditional B&B algorithms in large search spaces.

### A* Algorithm
- **Description**: A pathfinding algorithm that combines the strengths of Dijkstra's Algorithm and heuristics to find the shortest path efficiently.
- **Complexity**: O(E) where E is the number of edges.
- **Use Cases**: Widely used in AI for navigation and pathfinding in games.

# CIA-2 Minimax and Alpha-Beta Pruning Algorithms

## Overview

This repository provides an explanation of two fundamental algorithms used in decision-making processes for games and artificial intelligence: **Minimax** and **Alpha-Beta Pruning**. These algorithms are essential for optimizing decision-making in two-player zero-sum games where players alternately choose moves to maximize their chances of winning.

### Table of Contents
1. [Minimax Algorithm](#minimax-algorithm)
   - [How It Works](#how-it-works)
   - [Iteration Table](#iteration-table)
2. [Alpha-Beta Pruning Algorithm](#alpha-beta-pruning-algorithm)
   - [How It Works](#how-it-works-1)
   - [Iteration Table](#iteration-table-1)
3. [Conclusion](#conclusion)

## Minimax Algorithm

### How It Works

The Minimax algorithm works by recursively exploring all possible moves in a game tree. At each level of the tree:
- The maximizing player tries to choose the move that maximizes their score.
- The minimizing player tries to choose the move that minimizes the maximizing player’s score.

The algorithm evaluates the tree from the leaf nodes up to the root, using the following principles:
- **Maximizing:** The maximizing player aims to select the child node with the highest value.
- **Minimizing:** The minimizing player aims to select the child node with the lowest value.

### Iteration Table

| Iteration | Depth | Node Index | Maximizing/Minimizing | Leaf Value | Best Value | Alpha | Beta | Action                |
|-----------|-------|------------|-----------------------|------------|------------|-------|------|-----------------------|
| 1         | 3     | 0          | Maximizing            | -          | -∞         | -∞    | +∞  | Start Maximizing      |
| 2         | 2     | 0          | Minimizing            | -          | +∞         | -∞    | +∞  | Recur to Node 1      |
| ...       | ...   | ...        | ...                   | ...        | ...        | ...   | ...  | ...                   |
| 20        | 1     | 0          | Maximizing            | -          | 9          | 9     | +∞  | Final Optimal Value   |

## Alpha-Beta Pruning Algorithm

### How It Works

Alpha-Beta Pruning is an optimization technique for the Minimax algorithm. It reduces the number of nodes evaluated in the search tree by pruning branches that cannot influence the final decision:
- **Alpha** is the best value that the maximizing player can guarantee at that level or above.
- **Beta** is the best value that the minimizing player can guarantee at that level or above.

By comparing these values, the algorithm can skip evaluating branches that will not affect the outcome.

### Iteration Table

| Iteration | Depth | Node Index | Maximizing/Minimizing | Leaf Value | Best Value | Alpha | Beta | Action                |
|-----------|-------|------------|-----------------------|------------|------------|-------|------|-----------------------|
| 1         | 3     | 0          | Maximizing            | -          | -∞         | -∞    | +∞  | Start Maximizing      |
| 2         | 2     | 0          | Minimizing            | -          | +∞         | -∞    | +∞  | Recur to Node 1      |
| ...       | ...   | ...        | ...                   | ...        | ...        | ...   | ...  | ...                   |
| 20        | 1     | 0          | Maximizing            | -          | 9          | 9     | +∞  | Final Optimal Value   |

## Conclusion

The Minimax and Alpha-Beta Pruning algorithms are fundamental in creating AI that can play games strategically. The Minimax algorithm ensures that players can make the best possible moves, while Alpha-Beta Pruning optimizes this process, reducing the number of nodes that need to be evaluated, thus improving efficiency.

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
