'''
Created on 2013-11-03

@author: Joel
'''

import random
import time

def scramble (in_filename, out_filename):
    """ (str, str)
    Take the name of an input file in_filename, scramble the order of its 
    lines, and write this to a file with name out_filename
    """
    
    in_file = open(in_filename, 'r')
    out_file = open(out_filename, 'w') 
    
    # count the number of lines in the input file
    total_lines = sum(1 for line in in_file)
    
    # call a method to find the character indicies of each line
    character_indices = get_indices(in_file, total_lines)
    
    # call a method to generate a scrambled order of lines
    scrambled_line_order = get_scrambled_order(total_lines)
    
    # write the lines of in_file to out_file in the order prescribed by scrambled_line_order
    for index in scrambled_line_order:
        out_file.write(get_line(in_file, index, character_indices))
    
    # remove final trailing newline character from out_file
#     out_file.seek(0, 2)
#     out_file.truncate(out_file.tell() - 2)
    
    # clean up file memory
    in_file.close()
    out_file.flush()
    out_file.close()

def get_indices(in_file, number_of_lines):
    """ (file, int) --> array
    Return an array containing the indices of the beginnings of each line in in_file
    """
    
    # prepopulate an array with 0's
    indices = [0 for i in range (number_of_lines + 1)]
    
    # set starting values of index and line number
    current_index = 0
    line_num = 1
    
    # go to the beginning of the file
    in_file.seek(0)
    
    # iterate through the file line-by-line and save indicies
    for line in in_file:
        current_index += (len(line) + 1 -1)
        indices[line_num] = current_index
        line_num += 1
        
    # navigate to the last line and make sure it isn't truncated by a lack of newline character
    in_file.seek(indices[number_of_lines - 1])
    last_line = in_file.readline()
    if ('\n' not in last_line):
        indices[number_of_lines] = 0
        
    return indices

def get_scrambled_order(total_lines):
    """ (int) --> array
    Return an array containing the numbers 0 to total_lines - 1 in random order
    """
    
    scrambled_order = [[i] for i in range(total_lines)]
    random.shuffle(scrambled_order)
    return [item[0] for item in scrambled_order]
            
            
def get_line(in_file, line_num, indices):
    """ (file, int, array) --> str
    Return the line denoted by line_num in the in_file
    """
    
    # seek to the beginning of the line
    start_index = indices[line_num]
    in_file.seek(start_index)
    
    # read the line until the nextline character, than manually add a newline character
    return str(line_num + 1) + ':' + in_file.read(indices[line_num + 1] - start_index - 2 + 1) + '\n'

if __name__ == '__main__':
    start_time = time.time()
    
    scramble('superbible.txt', 'scrambled_superbible.txt')
#     scramble('test_s_input.txt', 'test_s_output.txt')

    print (time.time() - start_time, "seconds")
