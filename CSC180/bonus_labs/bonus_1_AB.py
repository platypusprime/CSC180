'''
Created on 2013-10-21

@author: Joel
'''

# A1
shopping_list = ['eggs', 'milk', 'chocolate chips', 'bread', 'chicken', 'love']

# A2
items = len(shopping_list) 
print(items)

# A3
print(shopping_list[2])

# A4
print(shopping_list[items - 1])
print(shopping_list[-1])

# A5
for item in shopping_list:
    print(item)
    
# B1
shopping_list.append('failure')
for item in shopping_list:
    print(item)

# B2
shopping_list.insert(3, 'cookies')
for item in shopping_list:
    print(item)

# B3
additional_list = ['blood', 'sweat', 'tears']
shopping_list.extend(additional_list)
for item in shopping_list:
    print(item)
    
# B4
shopping_list.sort()
for item in shopping_list:
    print(item)
    
# B5
shopping_list2 = shopping_list
shopping_list2.append('cthulu')
for item in shopping_list:
    print(item)
