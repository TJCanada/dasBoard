from defines import *
# x = int(input("what number is x\n"))
# y = int(input("what number is y\n"))
# char = input("what character is Char\n")


board = load_board("first_grid")
(pretty_print_board(board))


# current_block = [0,1]
currentBlock = {"x": 1, "y":1}

# currentBlock["x"]

while(True):
    direction = input("direction")
    currentBlock, board =  move(direction, currentBlock, board)
    pretty_print_board(board)
    print(currentBlock)