'''
Created on 2013-10-28

@author: Joel
'''

file_in = open('university_ranking2.txt', 'r')
lines = [line for line in file_in]
file_in.close();



file_out = open('university_ranking2.txt', 'w')
rank = 1
for line in lines:
    file_out.write(str(rank) + '. ' + line)
    rank += 1

file_out.flush()