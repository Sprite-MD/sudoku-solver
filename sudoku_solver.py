


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

def isValid(board):

    # Check Row
    for row in range(9):
        for column_value in range(9):
            if board == column_value:
                return False

    # Check Column

    for column in range(9):
        for row_value in range(9):
            if board == row_value:
                return False

    # Check Sub-grids
    