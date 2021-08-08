from random import randint
import time
import random

grid = []

for x in range(0,5):
    grid.append(["O"]*5)
print (grid)
def grid_layout (grid):
    for row in grid:
        " ".join(row)
print(grid_layout)    

def rand_row(board):
    return randint (0,len(board) -1)
    