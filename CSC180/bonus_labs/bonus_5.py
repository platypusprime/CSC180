'''
Created on 2013-11-25

@author: Joel
'''

import time
import random

# Part A
marks = [78, 81, 45, 91, 85, 79, 63, 86, 67, 96, 52, 60, 81, 83, 71, 90]
 
def insertion_sort(L):
    for n in range (1, len(L)):
        for i in range(0, n):
            if L[n] < L[i]:
                L.insert(i, L.pop(n)) 
    return L;
 
sorted_marks = insertion_sort(marks)
print(sorted_marks)

# Part B
marks = [78, 81, 45, 91, 85, 79, 63, 86, 67, 96, 52, 60, 81, 83, 71, 90]

def merge_sort(L):
    
    length = len(L)
    
    if length <= 1:
        return L
    
    a = merge_sort(L[0:int(length / 2)])
    b = merge_sort(L[int(length / 2):length])

    return merge(a, b)

def merge (a, b):
    
    merged_list = []
    
    i = 0;
    while (len(a) > 0 and len(b) > 0):
        if (a[0] < b[0]):
            merged_list.append(a.pop(0))
        else:
            merged_list.append(b.pop(0))
        i += 1
    
    return merged_list + a + b

sorted_marks = merge_sort(marks)
print(sorted_marks)

# Part C
start_time = time.time()
marks = [78, 81, 45, 91, 85, 79, 63, 86, 67, 96, 52, 60, 81, 83, 71, 90]
sorted_marks = insertion_sort(marks)
end_time = time.time()
print(end_time - start_time)
 
start_time = time.time()
marks = [78, 81, 45, 91, 85, 79, 63, 86, 67, 96, 52, 60, 81, 83, 71, 90]
sorted_marks = merge_sort(marks)
end_time = time.time()
print(end_time - start_time)

# Part D
def generate_random_test_case(N):
    return [random.randint(0,N) for x in range(N)]
 
def time_sorts(N, runs):
     
    total_time = 0
      
    for x in range(runs):
        list = generate_random_test_case(N)
        start_time = time.time()
        sorted_marks = insertion_sort(list)
        end_time = time.time()
        total_time += end_time - start_time
    print(total_time)
    print(total_time / (N * runs))
     
    total_time = 0
     
    for x in range(runs):
        list = generate_random_test_case(N)
        start_time = time.time()
        sorted_marks = merge_sort(list)
        end_time = time.time()
        total_time += end_time - start_time
    print(total_time)
    print(total_time / (N * runs))
 
time_sorts(10000,1)
time_sorts(100000,10)
time_sorts(100000,100)
time_sorts(1000000,1)
time_sorts(1000000,10)
time_sorts(1000000,100)
time_sorts(10000000,1)
time_sorts(10000000,10)
time_sorts(10000000,100)
