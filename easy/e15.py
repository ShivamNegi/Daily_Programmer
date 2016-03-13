with open("txtfile.txt", 'r') as f:
    print "Left justify."
    for line in f.readlines():
        print line,
    print "Right justify."
    size = 80
    f.seek(0)
    with open("righttxtfile.txt", 'w+') as f1:
        for line in f.readlines():
            f1.write(" " * (size - len(line)) + line)
