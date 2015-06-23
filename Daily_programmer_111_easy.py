sent = list(raw_input())
flag = 0
n_sent = []
"""for (i,ch) in enumerate(sent):
    if ch == '*':
        if i >0 and sent[i-1] != '*':
            sent.pop(i-1)
        if i < len(sent) and sent[i+1] != '*':
            sent.pop(i+1)            
for ch in sent:
    if ch != '*':
        n_sent.append(ch)
        """
l = len(sent)
i = 0
while i < l:
    if sent[i] == '*':
        if i > 0 and sent[i-1] != '*':
            sent.pop(i-1)
            l -= 1
        if i < l and sent[i+1] != '*':
            sent.pop(i+1)
            l -= 1           
    i += 1
for ch in sent:
    if ch != '*':
        n_sent.append(ch)

n_sent = ''.join(n_sent)            
print n_sent
