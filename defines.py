import chalk
def strToArr(string):
    array=[]
    for character in string:
        array.append(character)
    return array

def load_board(fn):
    with open(fn) as txt:
        rows = txt.readlines()
        board=[]
        
        for row in rows:
            str = row[:-1]
            ar = strToArr(str)
            board.append(ar)
    return board
        
        
        # what is fn,
        
def make_board(x,y,char):
    return [[char]*x for _ in range(y)]



def pretty_print_board(board):
    print("\n".join(["".join(row) for row in board]))

def move(direction, current_block, board):
    nextBlock = dict(current_block)

    if direction == "s":
        nextBlock["x"]+= 1
    if direction == "d":
        nextBlock["y"]+= 1
    if direction == "a":
        nextBlock["y"]-= 1 
    if direction == "w":
        nextBlock["x"]-= 1 
    if direction == "p":
        board[current_block["x"]][current_block["y"]] = "🔥" 
   
    nextBLockCharacter = board[nextBlock["x"]][nextBlock["y"]]
    touchingWall = nextBLockCharacter == "|" or nextBLockCharacter == "-"
    notmove = touchingWall or direction == "p"
    if not notmove:
        board[nextBlock["x"]][nextBlock["y"]] = chalk.cyan('o')
        if not direction == "p":
            board[current_block["x"]][current_block["y"]] = "x"
        return nextBlock, board

    return current_block, board
    
