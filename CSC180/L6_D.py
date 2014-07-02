'''
Created on 2013-11-03

@author: Joel
'''

import time

def descramble (in_filename, out_filename):
    """ (str, str)
    Take the name of an input file in_filename, descramble its contents 
    based on line numbers given in the file, and write this to a file with 
    name out_filename
    """
    
    in_file = open(in_filename, 'r')
    out_file = open(out_filename, 'w')
    
    # count the lines in the input
    total_input_lines = sum(1 for line in in_file)
    
    # call a method to find the indicies of each of the line in the order required
    indices = get_indices(in_file, total_input_lines)
    
    # iterate through the indicies and write the line indicated into out_file
    for index in indices:
        in_file.seek(index)
        # strip trailing newline characters and then add one manually
        line = in_file.readline()
#         print(line)
        out_file.write(line.split(':',1)[1])
#         out_file.write(line.rstrip('\n').split(':', 1)[1] + '\n')
    
    # remove final trailing newline character from the out_file
#     out_file.seek(0, 2)
#     out_file.truncate(out_file.tell() - 2)
    
    # clean up file memory
    in_file.close()
    out_file.flush()
    out_file.close()
            
def get_indices(in_file, number_of_lines):
    """ (file, int) --> array
    Return the the descrambled indices of a scrambled in_file with
    number_of_lines lines
    """
    
    # populate an array of length number_of_lines with 0's
    indices = [0 for i in range ((number_of_lines))]
    
    current_index = 0
    in_file.seek(0)
    
    for line in in_file:
        # save the current index to the line number indicated in the line
        indices[int(line.split(':', 1)[0]) - 1] = current_index
        current_index += (len(line)+1-1)
       
    return indices

if __name__ == '__main__':
    
    start_time = time.time()
   
    descramble('scrambled_superbible.txt', 'descrambled_superbible.txt')

    print (time.time() - start_time, "seconds")
