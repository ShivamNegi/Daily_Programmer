from random import shuffle
from copy import deepcopy


def reading(d):
    no = 0
    with open('in.txt', 'r') as f:
        for line in f.readlines():
            d[no] = line.split()
            no += 1


def finding(names, dnames, d):
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
        if flag and check_noloop(names, dnames):
            with open('out.txt', 'w') as f1:
                for i in range(len(names)):
                        f1.write(names[i] + "-->" + dnames[i] + "\n")
            break


def check_noloop(names, dnames):
    flag = True
    for i in range(int(len(names) / 2)):
        if dnames[names.index(dnames[i])] != names[i]:
            pass
        else:
            flag = False
            break
    return flag


def main():
    d = {}
    reading(d)
    names = []

    for name in d.values():
        for i in range(len(name)):
            names.append(name[i])

    dnames = deepcopy(names)
    shuffle(names)

    finding(names, dnames, d)

if __name__ == '__main__':
    main()
