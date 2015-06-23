sent = raw_input()
vowels = 'aeiou'
n_sent = []
removed = []
for ch in sent:
    if ch.lower() in vowels:
        removed.append(ch)
    elif ch !=' ':
        n_sent.append(ch)
n_sent = ''.join(n_sent)
removed = ''.join(removed)
print n_sent
print removed
