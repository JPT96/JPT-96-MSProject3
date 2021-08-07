class battleship(object):
    @staticmethod
    def build(head, length, direction):
        body= []

    def __init__(self,body):
        self.body = body
b = battleship.build((1,1),3,"S")        
def board_h_w (board_width, board_height, shots):
    header_bottom = print("+" + "-" * board_width + "+")
    print("+" + "-" * board_width + "+")
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
    header_bottom = print("+" + "-" * board_width + "+")
if __name__ == "__main__":
    shots = []
    while True:

        shoot = input("Orders Commander?\n")
        print(shoot)
        xstr, ystr = shoot.split(",")
        x = int(xstr)
        y = (ystr)
        shots.append((x,y))
        board_h_w(10,10,shots)