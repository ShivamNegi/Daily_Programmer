power = input("Enter the base: ")
no = input("Enter the number: ")
o_nos = [no]
def newnumber(no,power):
    sum = 0
    while (no != 0):
        sum += (no%10)**power
        no = no/10
    return sum
    
while True:
    no = newnumber(no,power)
    if no not in o_nos:
        o_nos.append(no)
    else:
        break

print "The sad cycle is :"
print (o_nos[o_nos.index(no):])
