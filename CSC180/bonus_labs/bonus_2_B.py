'''
Created on 2013-10-28

@author: Joel
'''

#1
f = open('my_profile.txt','w')

#2-5
f.write('Name: Nicolas Cage\nPhone: 416-111-1111\nCity: Toronto')
f.flush()

#6-7
f.seek(20)
f.write("Phone: 416-345-5555")
f.flush()

#8
f.seek(0)
f.write('Name: Nicolas Case Junior')
f.flush()
