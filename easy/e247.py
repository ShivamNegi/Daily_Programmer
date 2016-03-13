from random import shuffle
from copy import deepcopy


def check_loop():
    flag = True
    for i in range(int(len(names) / 2)):
        if dnames[names.index(dnames[i])] != names[i]:
            pass
        else:
            flag = False
            break
    return flag


d = {}
no = 0

while True:
    inp = input()
    if inp == 'False':
        break
    d[no] = inp.split()
    no += 1

names = []

for name in d.values():
    for i in range(len(name)):
        names.append(name[i])

dnames = deepcopy(names)

while True:
    shuffle(names)
    flag = True
    k = 0

    for i in range(len(d)):
        for j in range(len(d[i])):
            if names[k] not in d[i]:
                k += 1
            else:
                flag = False
                break
    if flag and check_loop():
        for i in range(len(names)):
                print (names[i] + "-->" + dnames[i])
        break
