#!usr/bin/env python

t = int(raw_input("Enter the no of nos: "))
ba = [False] * t

while True:
    try:
        no1, no2 = map(int, raw_input().split())
    except:
        break
    if no1 > no2:
        no1, no2 = no2, no1
    for j in range(no1, no2 + 1):
        ba[j] = not ba[j]
    # print ba

print "The number of switches on are", ba.count(True)
