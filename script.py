import time
import random
import copy

class gaming_board(object):
    def __init__(self,battleships,width,height):
        self.battleships = battleships
        self.width = width
        self.height = height
        self.shots = []

def shoot_shot(self,shot_loc):
    dmg_battleship = None
    is_hit = False 
    for b in self.battleships:
        index = b.body_index(shot_loc)
        if index is not None:
            is_hit = True
            b.hits[index] = True
            dmg_battleship = b
            break
    
    self.shots.append(shot(shot_loc, is_hit))
    return dmg_battleship
def game_finished(self):
    return all ([b.is_sunk() for b in self.battleships])    
    
class shot(object):
    def __init__(self,location,is_hit):
        self.location = location
        self.is_hit = is_hit

class battleship(object):
    @staticmethod
    def structure(tip,length,direction):
        body=[]
        for i in range(length):
            if direction == "S":

                element = (tip[0],tip[1] +i)
            elif direction == "N":
                element = (tip[0],tip[1] -i)
            elif direction == "E":
                element = (tip[0]+i, tip [1])   
            elif direction == "W":
                element = (tip[0],tip[1]+i)
            body.append(element)  
        return battleship(body,direction)    

def __init__(self,body,direction):
    self.body = body
    self.direction = direction
    self.hits = [False] * len(body)
def body_index(self,loc):
    try:
        return self.body.index(loc)
    except ValueError:
        return None    

def is_sunk (self):
    return all (self.hits)
    


