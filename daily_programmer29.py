inp = raw_input("Enter the name: ")
name = []
for ch in inp:
    if ch.isalpha() == 1:
        name.append(ch)
    else:
        break
name = "".join(name)
print name + ', ' + name + ' bo B%s' %(name[1:])
print 'Bonana Fanna fo F%s' %(name[1:])
print 'fee fy mo M%s' %(name[1:])
print inp
