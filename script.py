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
    return randint(0,len(board) -1)
def rand_coll(board):
    return randint(0,len(board[0]) -1) 

boat_row = rand_row
boat_coll = rand_coll

target_row = int(input("Target The Row:"))
target_coll = int(input("Target The Collum:"))
print (boat_coll)
print(boat_row)

if target_row == boat_row and target_coll == target_coll:
    print("Your Sub Is Sleeping With The Fishes!")
else:
    if target_row > range(5) or target_coll > range(5):
        print("Where Are You Aiming?")
    else:    
        print("You Whiffed Try Again!")
        grid[target_coll][target_row]="X"
        grid_layout(grid)
