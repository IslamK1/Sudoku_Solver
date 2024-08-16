#Algorithm for the solution using backtracking
#1. Find an empty square in the board
#2. Try all the possible numbers on that square 
#3. Find the one number that currently works
#4. Repeat 
#5. Backtrack(if current square doesn't work then return to the previous one and see if it works)


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


def solve(bo):
    #algorithm to solve a sudoku using recursion

    find = find_empty(bo)

    #base case of recursion(whrn the board is full)
    if not find: 
        return True 
    else: 
        row, col = find 
    
    #recursive case 
    for i in range(1, 10): 
        if valid(bo, i, (row, col)):
            bo[row][col] = i 

            if solve(bo): 
                return True 
            
            bo[row][col] = 0 
    
    return False 
    


def valid(bo, num, pos): 
    #function to check if the board is valid or not

    #check row 
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            #check every column in the row 
            return False 
    
    #check column 
    for i in range(len(bo)): 
        if bo[i][pos[1]] == num and pos[0] != i:
            #check every row in the column
            return False 
    
    #check box 
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos: 
                return False 
    
    return True


def print_board(bo): 
    #function to print board
    for i in range(len(bo)): 
        if i % 3 == 0 and i != 0: #if we are on the third row, print horizontal line
            print("- - - - - - - - - - - - -")
        
        for j in range(len(bo[0])): 
            if j % 3 == 0 and j != 0: 
                print(" | ", end="")

            if j == 8: 
                print(bo[i][j])
            else: 
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    #function to find and pick an empty square in the board
    #empty is 0
    for i in range(len(bo)): 
        for j in range(len(bo[0])): 
            if bo[i][j] == 0: 
                return (i, j) #row, col (y,x) 

    return None

print_board(board)
solve(board)
print("                         ")
print_board(board)