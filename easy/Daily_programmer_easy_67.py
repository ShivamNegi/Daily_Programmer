n = input("Enter the number: ")
machine = bin(n)
machine = machine[2:]
length = len(machine)
convert = machine + '0' * (32-length)
print convert
"""
integer = 0
for i in convert:
    integer +=  int(i)*(2**length)
    length -= 1
print length
"""
print int(convert,2)
