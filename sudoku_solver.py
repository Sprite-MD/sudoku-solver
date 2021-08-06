'''
1. Create check if num is valid at current slot after assignment
2. Create recursive function that inputs board
3. Check board for any unassigned slots. If true, cycle through 1-9 to check if any nums are valid
4. If all slots have been assigned and conform to rules, then return True

'''


board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def isValid(board, row, column, num):

    # Check Row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check Column
    for i in range(9):
        if board[i][column] == num:
            return False
    
    # Check Sub-grids
    for i in range(3):
        for j in range(3):
            pass

def empty_slot(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return True
    return False

def solve(board):
    row = 0
    column = 0

    # Base Case
    if not empty_slot(board):
        return True

    for num in range(1,10):
        
        
        
        if solve(board): return True # Number works
        
        board[row][column] == 0 # resets the slot to 0 if ^ did not work





    return False    # Should trigger backtracking