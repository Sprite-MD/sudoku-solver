'''
1. Find empty index 
2. Attempt to place digits 1-9 in index
3. Check if the digit is valid in current spot (yes = recursively repeat steps 1-3)
   if not, reset spot and go back to previous index
4. Once board is full, puzzle is complete

'''


board = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 3, 0, 8, 5], [0, 0, 1, 0, 2, 0, 0, 0, 0], [0, 0, 0, 5, 0, 7, 0, 0, 0], [0, 0, 4, 0, 0, 0, 1, 0, 0], [0, 9, 0, 0, 0, 0, 0, 0, 0], [5, 0, 0, 0, 0, 0, 0, 7, 3], [0, 0, 2, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 4, 0, 0, 0, 9]]


# Need to figure out subgrid
def is_valid(board, num, row, column):

    # Check Row
    for i in range(len(board[0])):
        if board[row][i] == num:
            return False

    # Check Column
    for i in range(len(board)):
        if board[i][column] == num:
            return False
    
    # Check Sub-grids
    top_left_row = 3 * (row // 3)
    top_left_column = 3 * (column // 3)

    for i in range(3):
        for j in range(3):
            if board[top_left_row + i][top_left_column + j] == num:
                return False



    return True


# Should work, returns the row and column of empty slot
def empty_slot(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i,j
    return -1,-1



def solve(board):
    

    row, column = empty_slot(board)
    
    if row == -1: return True




    for num in range(1,10):
        if is_valid(board, num, row, column):

            board[row][column] = num

            if solve(board): return True

            board[row][column] = 0

            


    return False    # Should trigger backtracking

def print_grid(board):
    for i, row in enumerate(board):
        for j, el in enumerate(row):
            print(el if el != 0 else ' ', end = '|' if j == 2 or j == 5 else ' ')
        print('\n-----+-----+-----' if i == 2 or i == 5 else '')
    print()

print_grid(board)
if solve(board): print_grid(board)
else: print('No Solution')






