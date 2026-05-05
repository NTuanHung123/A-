from typing import List, Tuple, Dict
import numpy as np
import heapq
from math import sqrt
import matplotlib.pyplot as plt

# 1. Tạo node
def create_node(position: Tuple[int, int], g=float('inf'), h=0.0, parent=None):
    return {
        'position': position,
        'g': g,
        'h': h,
        'f': g + h,
        'parent': parent
    }

# 2. Heuristic (Euclid)
def calculate_heuristic(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 3. Lấy hàng xóm hợp lệ
def get_valid_neighbors(grid, position):
    x, y = position
    rows, cols = grid.shape

    moves = [
        (x+1, y), (x-1, y),
        (x, y+1), (x, y-1),
        (x+1, y+1), (x-1, y-1),
        (x+1, y-1), (x-1, y+1)
    ]

    neighbors = []
    for nx, ny in moves:
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx, ny] == 0:
            neighbors.append((nx, ny))

    return neighbors

# 4. Tái tạo đường đi
def reconstruct_path(node):
    path = []
    while node:
        path.append(node['position'])
        node = node['parent']
    return path[::-1]

# 5. Thuật toán A*
def find_path(grid, start, goal):
    start_node = create_node(start, g=0, h=calculate_heuristic(start, goal))

    open_list = []
    heapq.heappush(open_list, (start_node['f'], start))

    open_dict = {start: start_node}
    closed_set = set()

    while open_list:
        _, current_pos = heapq.heappop(open_list)
        current_node = open_dict[current_pos]

        if current_pos == goal:
            return reconstruct_path(current_node)

        closed_set.add(current_pos)

        for neighbor_pos in get_valid_neighbors(grid, current_pos):
            if neighbor_pos in closed_set:
                continue

            tentative_g = current_node['g'] + calculate_heuristic(current_pos, neighbor_pos)

            if neighbor_pos not in open_dict:
                neighbor = create_node(
                    neighbor_pos,
                    g=tentative_g,
                    h=calculate_heuristic(neighbor_pos, goal),
                    parent=current_node
                )
                open_dict[neighbor_pos] = neighbor
                heapq.heappush(open_list, (neighbor['f'], neighbor_pos))

            elif tentative_g < open_dict[neighbor_pos]['g']:
                neighbor = open_dict[neighbor_pos]
                neighbor['g'] = tentative_g
                neighbor['f'] = tentative_g + neighbor['h']
                neighbor['parent'] = current_node

    return []

# 6. Hiển thị dạng text
def visualize_path(grid, path):
    grid_copy = np.copy(grid)

    for x, y in path:
        grid_copy[x][y] = 8

    for row in grid_copy:
        print(' '.join('*' if cell == 8 else str(cell) for cell in row))

# 7. Vẽ đồ thị
def plot_grid(grid, path):
    fig, ax = plt.subplots()

    ax.imshow(grid, cmap='Greys')

    if path:
        x = [p[1] for p in path]
        y = [p[0] for p in path]

        ax.plot(x, y, marker='o')

        ax.plot(x[0], y[0], marker='s')
        ax.plot(x[-1], y[-1], marker='s')

    plt.show()

# 8. MAIN
if __name__ == "__main__":
    # Tạo grid 20x20
    grid = np.zeros((20, 20))

    # Tạo tường ngang
    grid[10, :] = 1

    # Tạo tường dọc
    grid[:, 10] = 1

    # Chừa lối đi
    grid[10, 5] = 0
    grid[15, 10] = 0

    start = (0, 0)
    goal = (19, 19)

    path = find_path(grid, start, goal)

    print("Đường đi:")
    print(path)

    print("\nGrid:")
    visualize_path(grid, path)

    plot_grid(grid, path)