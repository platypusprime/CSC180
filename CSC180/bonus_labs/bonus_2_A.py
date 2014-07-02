'''
Created on 2013-10-28

@author: Joel
'''

# 1
in_file = open('university_ranking.txt', 'r')

# 2
print(in_file.read())

# 3
l = in_file.tell()
print(l)
# yes, this is the number of characters in the file added to twice the number of lines in the file

# 4
in_file.seek(0)
for line in in_file:
    print(line,end='')

print()
# 5
in_file.seek(in_file.tell() - 5)
print(in_file.read(1))
in_file.seek(20)
print(in_file.read(2))
in_file.seek(l - 3)
print(in_file.read(3))
print(in_file.read(2))

# 6
in_file.seek(0)
print(in_file.readline())

# 7
in_file.close()
