from string import ascii_lowercase
alpha = ascii_lowercase
n = input()
output = []
for i in range(n):
    sent = raw_input()
    flag = True
    for ch in alpha:
        if ch in sent.lower():
            pass
        else:
            flag = False
            break
    if flag == True:
        output.append(1)
    else:
        output.append(0)
for o in output:
    if o == 1:
        print "True"
    else:
        print "False"
