sample = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

#check backwards
def check_backwards(board, row, col):
    try:
        if (col -3 < 0): return 0
        if "".join([board[row][col], board[row][col-1], board[row][col-2], board[row][col-3]]) == "XMAS":
            return 1
        return 0
    except IndexError:
        return 0
    
#check forward
def check_forwards(board, row, col):
    try:
        if "".join([board[row][col], board[row][col+1], board[row][col+2], board[row][col+3]]) == "XMAS":
            return 1
        return 0
    except IndexError:
        return 0
    
#check up
def check_up(board, row, col):
    try:
        if (row-3 < 0 ): return 0

        if "".join([ board[row][col], board[row-1][col], board[row-2][col], board[row-3][col]]) == "XMAS":
            return 1
        return 0
    except IndexError:
        return 0
    
#check down
def check_down(board, row, col):
    try:
        if "".join([ board[row][col], board[row+1][col], board[row+2][col], board[row+3][col]]) == "XMAS":
            return 1
        return 0
    except IndexError:
        return 0

#check diagonal up
def check_diagonal_up(board, row, col):
    try:
        if (row-3 < 0 ): return 0
        if "".join([ board[row][col], board[row-1][col+1], board[row-2][col+2], board[row-3][col+3]]) == "XMAS":
            return 1
        return 0
    except IndexError:
        return 0
    
#check diagonal down
def check_diagonal_down(board, row, col):
    try:
        if (col -3 < 0): return 0
        if "".join([ board[row][col], board[row+1][col-1], board[row+2][col-2], board[row+3][col-3]]) == "XMAS":
            return 1
        return 0
    except IndexError:
        return 0
    
#check diagonal neg up
def check_diagonal_neg_up(board, row, col):
    try:
        if (row-3 < 0 or col -3 < 0): return 0
        if "".join([ board[row][col], board[row-1][col-1], board[row-2][col-2], board[row-3][col-3]]) == "XMAS":
            return 1
        return 0
    except IndexError:
        return 0
    
#check diagonal neg down
def check_diagonal_neg_down(board, row, col):
    try:
        if "".join([ board[row][col], board[row+1][col+1], board[row+2][col+2], board[row+3][col+3]]) == "XMAS":
            return 1
        return 0
    except IndexError:
        return 0

def check_x_mas(board,row,col):
    if (row-1 < 0 or row+1 >= len(board)): return 0
    if (col-1 < 0 or col+1 >= len(board[0])): return 0

    pos_diag = False
    neg_diag = False

    if ("".join([board[row+1][col-1], board[row][col], board[row-1][col+1]]) == 'MAS'): pos_diag = True
    if ("".join([board[row+1][col-1], board[row][col], board[row-1][col+1]]) == 'SAM'): pos_diag = True

    if ("".join([board[row-1][col-1], board[row][col], board[row+1][col+1]]) == 'MAS'): neg_diag = True
    if ("".join([board[row-1][col-1], board[row][col], board[row+1][col+1]]) == 'SAM'): neg_diag = True

    return 1 if (pos_diag and neg_diag) else 0


def process_2(lines):
    count = 0
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if (lines[row][col] == 'A'):
                count += check_x_mas(lines,row,col)
    print(count)

def process_1(lines):
    count = 0
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if (lines[row][col] == 'X'):
                count += check_backwards(lines, row, col)
                count += check_forwards(lines, row, col)
                count += check_up(lines, row, col)
                count += check_down(lines, row, col)
                count += check_diagonal_down(lines, row, col)
                count += check_diagonal_neg_down(lines, row, col)
                count += check_diagonal_neg_up(lines, row, col)
                count += check_diagonal_up(lines, row, col)
    print(count)


def main():
    with open('./inputs/2024/day4.txt') as f:
        lines = [list(l.strip()) for l in f.readlines()]
        #process_2([list(l) for l in sample.split('\n')[1:-1]])
        process_2(lines)

if __name__ == '__main__':
    main()
