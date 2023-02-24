import random
import time
import os


WIDTH = 60
HEIGHT = 20


INITIAL_PROBABILITY = 0.2


ALIVE = "#"
DEAD = "."

def initialize_grid():
    """Initialize the grid with random alive and dead cells"""
    grid = []
    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            if random.random() < INITIAL_PROBABILITY:
                row.append(ALIVE)
            else:
                row.append(DEAD)
        grid.append(row)
    return grid

def print_grid(grid):
    """Print the grid to the console"""
    os.system("clear")
    for row in grid:
        print("".join(row))

def get_neighbours(grid, x, y):
    """Get the list of neighbours for a cell"""
    neighbours = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            neighbour_x = x + i
            neighbour_y = y + j
            if neighbour_x < 0 or neighbour_x >= WIDTH:
                continue
            if neighbour_y < 0 or neighbour_y >= HEIGHT:
                continue
            neighbour = grid[neighbour_y][neighbour_x]
            neighbours.append(neighbour)
    return neighbours

def get_next_state(grid, x, y):
    """Calculate the next state of a cell"""
    cell = grid[y][x]
    neighbours = get_neighbours(grid, x, y)
    num_alive_neighbours = neighbours.count(ALIVE)
    if cell == ALIVE:
        if num_alive_neighbours < 2 or num_alive_neighbours > 3:
            return DEAD
        else:
            return ALIVE
    else:
        if num_alive_neighbours == 3:
            return ALIVE
        else:
            return DEAD

def get_next_grid(grid):
    """Calculate the next state of the entire grid"""
    next_grid = []
    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            next_state = get_next_state(grid, x, y)
            row.append(next_state)
        next_grid.append(row)
    return next_grid


grid = initialize_grid()


while True:
    print_grid(grid)
    grid = get_next_grid(grid)
    time.sleep(0.1)
