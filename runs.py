from board import *
from character import *
# x = int(input("what number is x\n"))
# y = int(input("what number is y\n"))
# char = input("what character is Char\n")


board = load_board("first_grid")
pretty_print_board(board)


# current_block = [0,1]
currentBlock = {"x": 1, "y": 1}

# {"move": move, "location": getLocation, "board": getBoard}
character = characterFactory(currentBlock, board)

print(character)

# currentBlock["x"]

while(True):
    direction = input("direction")
    character["move"](direction)
    pretty_print_board(character["board"]())
    print(character['location']())
