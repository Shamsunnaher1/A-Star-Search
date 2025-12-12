class Node:
    def __init__(self, row, col, g, h, parent=None):
        self.row = row
        self.col = col
        self.G = g
        self.H = h
        self.F = g + h
        self.parent = parent

def manhattan(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

def a_star(grid, start, target):
    rows = len(grid)
    cols = len(grid[0])
    sr, sc = start
    tr, tc = target

    open_list = [Node(sr, sc, 0, manhattan(sr, sc, tr, tc))]
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    found = False

    while open_list:
        open_list.sort(key=lambda x: x.F)
        current = open_list.pop(0)

        if (current.row, current.col) == (tr, tc):
            path = []
            node = current
            while node:
                path.append((node.row, node.col))
                node = node.parent
            path.reverse()
            print(f"Path found with cost {current.G} using A*")
            print("Shortest Path:", path)
            found = True
            break

        visited[current.row][current.col] = True

        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for dr, dc in directions:
            nr, nc = current.row + dr, current.col + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 0:
                g_cost = current.G + 1
                h_cost = manhattan(nr, nc, tr, tc)
                open_list.append(Node(nr, nc, g_cost, h_cost, current))

    if not found:
        print("Path not found using A*")

file = open("input1.txt", "r")
line = file.readline().strip().split()
R, C = int(line[0]), int(line[1])

grid = []
for _ in range(R):
    row = list(map(int, file.readline().strip().split()))
    grid.append(row)

start_line = file.readline().strip().split()
sr, sc = int(start_line[0]), int(start_line[1])

target_line = file.readline().strip().split()
tr, tc = int(target_line[0]), int(target_line[1])

file.close()

a_star(grid, (sr, sc), (tr, tc))
