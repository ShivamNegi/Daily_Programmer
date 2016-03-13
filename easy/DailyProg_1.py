no = raw_input('Enter the numbers : ')
no = no.split()

for n in no:
    j = no.count(n)
    while j > 1:
        no.remove(n)
        j -= 1

no.sort()
print no
end = raw_input("Press Enter")
