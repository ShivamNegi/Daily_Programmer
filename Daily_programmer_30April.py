vowels = 'AEIOUY'
vowels = list(vowels)
sent = raw_input()
rover_sent = []
for ch in sent:
    flag = 0
    if ch.upper() in vowels:
        rover_sent.append(ch)
    elif ch.isalpha():
        if ch.isupper():
        `    flag = 1
        rover_sent.append(ch)
        rover_sent.append('o')
        if flag == 0:
            rover_sent.append(ch)
        else:
            rover_sent.append(ch.lower())
    else:
        rover_sent.append(ch)

print "".join(rover_sent)

