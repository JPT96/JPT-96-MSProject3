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
def rand_coll(board):
    return randint (0,len(board[0]) -1) 

boat_row = rand_row
boat_coll = rand_coll

target_row = int(input("Target The Row:"))
target_coll = int(input("Target The Collum:"))
