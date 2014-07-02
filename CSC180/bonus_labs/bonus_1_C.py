'''
Created on 2013-10-21

@author: Joel
'''

import math

marks = [78, 81, 45, 91, 85, 79, 63, 86, 67, 96, 52, 60, 81, 83, 65, 71, 90]

def get_average(marks):
    
    total = 0
    for i in marks:
        total += i
    
    return total / len(marks)


def get_medium(marks):

        
    med_index = math.ceil(len(marks)/2)
    marks.sort()
    return marks[med_index]
    


print(get_average(marks))
print(get_medium(marks))
