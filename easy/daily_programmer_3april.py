cmd = raw_input('')
start = input()
terms = input()
for j in range(terms):
    i=0
    while i < len(cmd):
        if cmd[i] == '+':
            k = i + 1
            while not (cmd[i].isdigit()):
                i+=1
            a = cmd[k:i+1]
            start = start + (int(a))
        elif cmd[i] == '-':
            k = i + 1
            while not cmd[i].isdigit():
                i+=1
            a = cmd[k:i+1]
            start = start - (int(a))
        elif cmd[i] == '*':
            k = i + 1 
            while not cmd[i].isdigit():
                i+=1
            a = cmd[k:i+1]
            start = start * (int(a))
        elif cmd[i] == '/':
            k = i + 1
            while not cmd[i].isdigit():
                i+=1
            a = cmd[k:i+1]
            start = start / (int(a))
        i+=1
    print('Term '+`j+1`+': '+`start`)

