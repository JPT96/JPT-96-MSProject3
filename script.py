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
  
class players(object):
    def __init__(self, name, shot_fir):
        self.name = name
        self.shot_fir = shot_fir

def basics (gaming_board,reveal_battleships=False):
    header_footer = "+" + "-" * gaming_board.width + "+"
    print(header_footer)
# creating empty board
    
    board = []
    for _ in range(gaming_board.width):
        board.append([None for _ in range (gaming_board.height)])
    if reveal_battleships:
        for b in gaming_board.battleships:
            for i, (x, y) in enumerate(b.body):
                if b.direction == "N":
                    char = ("v","|", "^")
                elif b.direction == "S":
                    char = ("^","|","v")
                elif b.direction =="W":
                    char (">","=","<")
                elif b.drection == "E":
                    char ("<","=",">") 
                else:
                    raise "invaild placement"    

                if i ==0:
                    ch = char[0]
                elif i == len(b.body) - 1:
                    ch = char[2]
                else:
                    ch = char[1]
                board[x][y] = ch                      
# add the shooting now

        for sh in gaming_board.shots:
            x, y = sh.location
            if sh.is_hit:
                ch = "X"
        else:
            ch = "O"
            board[x][y] = ch
        for y in range (gaming_board.height):
            row=[]
            for x in range (gaming_board.width):
                row.append(board[x][y] or " ")
            print("|"+"".join(row)+"|")
        print(header_footer)        

def anounc_eve(event_type,metadata={}):
    if event_type == "Game_Over":
        print("%s Wins The Game" % metadata["Player"])
    elif event_type =="New_Turn":
        print("%s Your Turn" % metadata ["Player"])
    elif event_type == "Miss":
        print("%s Whiffed" % metadata["Player"])
    elif event_type == "battleship_sunk":
        print("%s Sunk a BattleShip" % metadata ["Player"])
    elif event_type == "battleship_hit":
        print("%s Pinged a boat" % metadata ["Player"])
    else:
        print("WHO Knows what just happened: %s" % event_type)

def anounc_nothing(event_type,metadata={}):
    pass   
#creating Ai shooting now

def ai_shooting(gaming_board):
    x = random.randint(0, gaming_board.width - 1)
    y = random.randint(0, gaming_board.height -1)
    return(x,y)
#person shooting now
def person_shooting(gaming_board):
    h_shot= input("Where Now Commander?\n")
    xstr, ystr = h_shot.split(",")
    x= int(xstr)
    y = int(ystr)

    return(x,y)
    




