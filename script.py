import time
import random
import copy

class gaming_board(object):
    def __init__(self,battleships,width,height):
        self.battleships = battleships
        self.width = width
        self.height = height
        self.shots = []
        


