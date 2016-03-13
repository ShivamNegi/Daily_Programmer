no = int(raw_input())

while no != 1:
    if no % 3 == 1:
        print no, -1
        no = (no - 1) / 3
    elif no % 3 == 2:
        print no, 1
        no = (no + 1) / 3
    else:
        print no, 0
        no = no / 3

print 1
