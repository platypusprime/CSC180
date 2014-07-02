'''
Created on 2013-11-04

@author: Joel
'''

# 1
dict = {}

# 2
dict['name'] = 'Joel'

# 3
dict['number'] = 1000544574

# 4
dict['course'] = 'csc180'

# 5
print(dict)
print()

#6
for item in dict.items():
    print(item)
print()
    
#7
del dict['course']

#8
for item in dict.items():
    print(item)