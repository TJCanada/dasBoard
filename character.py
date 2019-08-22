

def characterFactory(current_block, board):
    location = current_block
    bag = []
    board = board

    def move(direction):
        nextBlock = dict(current_block)
        if direction == "s":
            nextBlock["x"] += 1
        if direction == "d":
            nextBlock["y"] += 1
        if direction == "a":
            nextBlock["y"] -= 1
        if direction == "w":
            nextBlock["x"] -= 1
        if direction == "p":
            board[current_block["x"]][current_block["y"]] = "🔥"

        nextBLockCharacter = board[nextBlock["x"]][nextBlock["y"]]
        touchingWall = nextBLockCharacter == "|" or nextBLockCharacter == "-"
        notmove = touchingWall or direction == "p"
        if not notmove:
            board[nextBlock["x"]][nextBlock["y"]] = 'o'
            if not direction == "p":
                board[current_block["x"]][current_block["y"]] = "x"
                location = nextBlock

    def getLocation():
        return location

    def getBoard():
        return board

    return {"move": move, "location": getLocation, "board": getBoard}
