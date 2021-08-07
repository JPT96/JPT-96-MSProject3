def board_h_w (board_width, board_height, shots):
    header_bottom = print("+" + "-" * board_width + "+")
    print("+" + "-" * board_width + "+")
    for y in range (board_height):
        row = []
        for x in range(board_width):
            if (x,y) in shots:
                row.append("X")
        print("¦" + " " * board_width)
    header_bottom = print("+" + "-" * board_width + "+")
if __name__ == "__main__":
    board_h_w(10,10)
    shoot = input("Orders Commander?\n")
    print(shoot)
    xstr, ystr = shoot.split(",")
    x = int(xstr)
    y = (ystr)
    