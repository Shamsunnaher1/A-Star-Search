# A* Search Algorithm for Grid Pathfinding

## Overview
This Python program finds the shortest path in a 2D grid from a start cell to a target cell using the A* search algorithm. It moves up, down, left, or right through empty cells (0) and avoids walls (1). The program uses the Manhattan distance as a heuristic to guide the search efficiently.

## Input
The program reads input from a file named `input1.txt` in the following format:

R C
<row 1 values>
<row 2 values>

<row R values>
sr sc
tr tc

- R and C are the number of rows and columns.
- Each grid row contains 0 (empty cell) or 1 (wall).
- sr sc are the start cell coordinates (row, column).
- tr tc are the target cell coordinates (row, column).

### Example

4 4
0 0 0 0
1 1 0 1
0 0 0 0
0 1 1 0
0 0
3 3

## Output
- If a path exists, the program prints:
Path found with cost <cost> using A*
Shortest Path: [(r1,c1), (r2,c2), ..., (tr,tc)]

- If no path exists, it prints:
Path not found using A*


## How It Works
1. The program starts from the given start cell and adds it to the list of cells to explore.
2. At each step, it selects the cell with the lowest total cost F = G + H.
   - G = cost from the start.
   - H = Manhattan distance to the target.
3. It explores neighboring cells (up, down, left, right) that are empty and not visited.
4. The process repeats until the target is reached or no more cells are left to explore.
5. The program reconstructs and prints the shortest path if found.

## Usage
1. Create an `input1.txt` file with the grid and start/target positions.
2. Run the Python script:



