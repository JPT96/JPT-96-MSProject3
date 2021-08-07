class battleship(object):
    @staticmethod
    def build(head, length, direction):
        body= []
        for i in range (length):
            if direction == "N":
                element = (head[0], head[1] - i) 
            elif direction == "S":
                element = (head[0], head[1] + i)
            elif direction == "W":
                element = (head[0] -i, head[1])
            elif direction == "E":
                element = (head[0] +i,head[1])
            body.append(element)
        return battleship(body)                  


    def __init__(self,body):
        self.body = body
b = battleship.build((1,1),3,"S")        
def board_h_w (board_width, board_height, shots):
    header_bottom = "+" + "-" * board_width + "+"
    print(header_bottom)
    shots_set = set(shots)
    for y in range (board_height):
        row = []
        for x in range(board_width):
            if (x,y) in shots_set:
                sh = "X"
            else:
                sh = " "
                row.append(sh)
        print ("|" + "".join(row) + "|")        
        print("|" + " " * board_width)
    print(header_bottom)
def render_battleships(board_width,board_height, battleships):
    header_bottom = "+" + "-" * board_width + "+"
    print(header_bottom)
    #build empty board
    board = []
    for x in range(board_width):
        row = []
        for y in range (board_height):
            row.append(None)
        board.append(row)
        #add the battleships
    for b in battleships:
        for x, y in b.body:  
            board [x] [y] = "O"
    for y in range(board_height):
        row = []
        for x in range(board_width):
            row.append(board[x][y] or " ")
        print("|"+"".join(row) + "|")    

    print(board)
    print(header_bottom)    





if __name__ == "__main__":
    battleships = [
        battleship.build((3,4),2,"N"),
        battleship.build((4,8),4,"N"),
        battleship.build((1,1),5,"E"),
        battleship.build((1,1),4,"W")
    ]    
    for b in battleships:
        print(b.body)
    render_battleships(10,10, battleships) 



    shots = []
    while True:

        shoot = input("Orders Commander?\n")
        print(shoot)
        xstr, ystr = shoot.split(",")
        x = int(xstr)
        y = (ystr)
        shots.append((x,y))
        board_h_w(10,10,shots)