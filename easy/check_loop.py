with open('out.txt', 'r') as f:
    d = {}
    for line in f.readlines():
        x, y = line.split('->')
        d[x] = y[:len(y) - 1]
    flag = False
    for key in d.keys():
        if d[key] == d[d[key]]:
            flag = True
            break
    print (flag)
