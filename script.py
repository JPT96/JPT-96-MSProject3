def board_h_w (board_width, board_height):
    print("+" + "-" * board_width + "+")
if __name__ == "__main__":
    board_h_w(10,10)
    shoot = input("Orders Commander?\n")
    print(shoot)
    xstr, ystr = shoot.split(",")
    x = int(xstr)
    y = (ystr)
