board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

def print_board(bo):
    for i in range(len(bo)):
        if i%3 == 0 and i!=0:
            print("-----------------------")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")
            
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j); #return row,col of the empty square
    return None


def isValid(bo, position, number):
    #Check the row first
    for i in range(len(bo[0])):
        if bo[position[0]][i] == number and position[1] != i:
            return False
    
    #Check the column
    for i in range(len(bo)):
        if bo[i][position[1]] == number and position[0] != i:
            return False
    
    #Check the whole box
    x = position[1] // 3
    y = position[0] // 3

    for i in range(y*3, y*3 + 3):
        for j in range(x*3, x*3 + 3):
            if bo[i][j] == number and (i,j) != position:
                return False
    
    return True

def solve(bo):
    find = find_empty(bo)
    if find:
        row,col = find
    else:
        return True
    
    for i in range(1, 10):
        if(isValid(bo,(row,col),i)):
            bo[row][col] = i

            if(solve(bo)):
                return True
            
            bo[row][col] = 0;
    
    return False
    


print_board(board)
solve(board)
print("SOLVED")
print_board(board)