inp1 = raw_input("Enter the word to be sorted: ")
inp2 = raw_input("Enter the word we want to get: ")
count = 0
from random import shuffle
while True:
    if inp1  != inp2:
        inp1 = list(inp1)
        shuffle(inp1)
        inp1 = ''.join(inp1)
        count += 1
    else:
        break
print count
