'''
Created on 2013-11-04

@author: Joel
'''

# 1
dict = {}

# 2
file = open('inventory_sample2.txt', 'r')

# 3
for line in file:
    pair = line.split(', ', 1)
    if pair[0] in dict:
        print('Duplicate Entry - ' + pair[0])
        dict[pair[0]] = dict[pair[0]] + int(pair[1].rstrip())
    else:
        dict[pair[0]] = int(pair[1].rstrip())
    
# 4
print(dict)

# 5
file.close()
