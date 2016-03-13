consonants = 'bcdfghjklmnpqrstvwxz'
sent = raw_input("Enter the sentence: ")
rover_sent = []
for ch in sent:
    flag = 0
    if ch.lower() in consonants:
        if ch.isupper():
            flag = 1
        rover_sent.append(ch)
        rover_sent.append('o')
        if flag ==1:
            rover_sent.append(ch.lower())
        else:
            rover_sent.append(ch)
    else:
        rover_sent.append(ch)        
print "".join(rover_sent)
