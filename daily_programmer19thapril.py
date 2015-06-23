data = []
a_z = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = input()
for i in range(n):
    user = []
    print "User%s:"%(a_z[i])    
    user.append(input())
    user.append('User%s'%(a_z[i]))
    data.append(user)

data.sort()

print
for i in range(n):
    print data[i][1],str(data[i][0])

from math import floor
datan = []
for i in range(n):
    if i==0:
        datan.append(60-data[i][0])
    else:
        datan.append(60-(data[i][0]-data[i-1][0]))
    datan[i]=floor(datan[i])

print
for i in range(n):
    print data[i][1],str(datan[i])

    
