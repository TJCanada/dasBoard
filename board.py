# import chalk


def strToArr(string):
    array = []
    for character in string:
        array.append(character)
    return array


def load_board(fn):
    with open(fn) as txt:
        rows = txt.readlines()
        board = []

        for row in rows:
            str = row[:-1]
            ar = strToArr(str)
            board.append(ar)
    return board

    # what is fn,


def make_board(x, y, char):
    return [[char]*x for _ in range(y)]


def pretty_print_board(board):
    print("\n".join(["".join(row) for row in board]))
