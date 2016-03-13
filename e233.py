
def converter(inp):
    emptysq = [["    "]] * 3
    dottedsq = [["+--+"], ["|  |"], ["+--+"]]
    output = []

    for row in inp:
        for ch in row:
            if(ch == " "):
                output.append(emptysq)
            else:
                output.append(dottedsq)

    return output


inpstart = []
lines = int(raw_input())

for i in range(lines):
    inp = raw_input()
    inpstart.append(inp)

output = converter(inpstart)

for row in output:
    for out in row:
        print out,
