
def brutef(n, l, li, no):
    if l > 0:
        for k in li:
            n.append(k)
            brutef(n, l - 1, li, no)
    elif int("".join(n)) == no:
        global count
        count += 1


no = int(raw_input())
l = len(bin(no)[2:])
li = [x for x in range(3)]
n = []
count = 0
brutef(n, l, li, no)
print count
