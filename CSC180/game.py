'''
Created on 2013-11-18

@author: Joel
'''

import math

grid = None
grid_size_l = None
grid_size_s = None

def play ():
    """ Begin a new game 
    """
    
    # access globals
    global grid
    global grid_size_l
    global grid_size_s
    
    # find the size of the grid
    valid_n = ['4', '9', '16'];    
    while not type(grid_size_l) == int:
        grid_size_l = input('Enter size of grid (n): ')
        if grid_size_l in valid_n:
            grid_size_l = int(grid_size_l)
            grid_size_s = int(math.sqrt(grid_size_l))
            break
        print('You have entered an invalid grid size!')
    
    # create grid of 0's
    grid = [[0 for x in range(grid_size_l)] for x in range(grid_size_l)]
    
    # set turn number to 0
    turn = 0;
    players = ['A', 'B']
    
    # check for wins at the beginning of each turn
    while check_win() == 0:
        
        # ask player for move until a valid move is entered
        while True:
            input_buffer = input ('Player ' + players[turn % 2] + ' enter a move: ')
            
            # checks for special command inputs
            if input_buffer == 's':
                save()
                continue
            if input_buffer == 'q':
                return
            
            # translates input into a move
            row, column, value = map(lambda x:int(x), input_buffer.replace(' ', '').split(','))
    
            # ask for move again in case of an invalid move
            if not check_move(row, column, value):
                continue
            
            # make and display changes to the grid
            grid[row][column] = value
            print_grid()
            turn += 1
            break
        
    # check for win conditions at the end of the game loop
    if check_win == 2:
        print ("Game has resulted in a tie")
    else:
        print("Player " + players[(turn - 1) % 2] + " has won")

    
def check_move(row, column, value):
    """ (int, int, int) -> bool
    Check whether a move is valid
    """
    
    global grid
    global grid_size_l
    global grid_size_s
    
    # check if cell occupied
    if grid[row][column] != 0:
        return False
    
    # check if value out of range
    if value > grid_size_l or value < 1:
        return False
    
    # check if value already in row
    if value in grid[row]:
        return False
    
    # check if value already in column
    if value in [grid[x][column] for x in range(grid_size_l)]:
        return False
    
    # check if value already in box
    for x in range(int(row / grid_size_s) * grid_size_s, (int(row / grid_size_s) + 1) * grid_size_s):
        for y in range(int(column / grid_size_s) * grid_size_s, (int(column / grid_size_s) + 1) * grid_size_s):
            if grid[x][y] == value:
                return False
    
    # if none of the checks are triggered, then the move is valid
    return True

def check_win ():
    """ () -> int
    Check if the game ends in a win, a tie, or not at all
    """
    
    global grid
    global grid_size_l
    global grid_size_s

    # check for a tie
    if grid_filled():
        return 2

    # search for possible moves
    for row in range(grid_size_l):
        for column in range(grid_size_l):
            for value in range(grid_size_s + 1):
                if check_move(row, column, value):
                    return 0
    
    # otherwise, someone has won
    return 1
    
def grid_filled ():
    """ () -> bool
    Check if all spaces in the grid are filled
    """
    global grid
    
    for row in grid:
        for cell in row:
            if cell == 0:
                return False
    return True

def print_grid():
    """ Print the current game grid to console
    """
    
    global grid
    global grid_size_l 
    global grid_size_s
    
    # handle 2-digit spacing
    spaces = 1
    if grid_size_l >= 10:
        spaces = 2
    
    for row_num in range(grid_size_l):
        row_string = ''
        for col_num in range(grid_size_l):
            row_string += str(grid[row_num][col_num])
            if col_num != (grid_size_l - 1):
                
                # add a vertical bar every third character
                if (col_num + 1) % grid_size_s == 0:
                    row_string += (spaces - int(grid[row_num][col_num] / 10) - 1) * ' ' + '|'
                # add appropriate spacing otherwise
                else:
                    row_string += (spaces - int(grid[row_num][col_num] / 10)) * ' '
        print (row_string.rstrip())
        
        # print horizontal line
        if (row_num + 1) % grid_size_s == 0 and row_num != (grid_size_l - 1):
            print('-' * (grid_size_l * (spaces + 1) - 1))
    
def save():
    """ Save the current game grid to user-specified file
    """
    
    global grid
    global grid_size_l 
    global grid_size_s
    
    file = open(input('Enter the name of the file: '), 'w')
    
    # handle 2-digit spacing
    spaces = 1
    if grid_size_l >= 10:
        spaces = 2
    
    for row_num in range(grid_size_l):
        row_string = ''
        for col_num in range(grid_size_l):
            row_string += str(grid[row_num][col_num])
            if col_num != (grid_size_l - 1):
                
                # add a vertical bar every third character
                if (col_num + 1) % grid_size_s == 0:
                    row_string += (spaces - int(grid[row_num][col_num] / 10) - 1) * ' ' + '|'
                # add appropriate spacing otherwise
                else:
                    row_string += (spaces - int(grid[row_num][col_num] / 10)) * ' '
        file.write(row_string.rstrip())
        
        # print horizontal line
        if (row_num + 1) % grid_size_s == 0 and row_num != (grid_size_l - 1):
            file.write('\n' + '-' * (grid_size_l * (spaces + 1) - 1))
        if row_num + 1 < grid_size_l:
            file.write('\n')