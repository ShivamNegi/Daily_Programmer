i_maths = raw_input("Input 1: ")
start = int(raw_input("Input 2: "))
end = int(raw_input("Input 3: "))

maths = i_maths.split(" ")

term = 0
math = start

print ""
print "Term 0 :", start

while term < end:
    for operator in maths:
        if operator[0] == "+":
            math += int(operator[1:])
        elif operator[0] == "-":
            math -= int(operator[1:])
        elif operator[0] == "*":
            math *= int(operator[1:])
        elif operator[0] == "/":
            math //= int(operator[1:])
    term += 1
    print "Term", term, ":", math
