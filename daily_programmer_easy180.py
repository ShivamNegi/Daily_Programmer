term = list('1')
n_term = []
n = input("Enter the term you want - ")
'''count = 0'''
for i in range(n-1):    
    n_term = []
    count = 0
    p_no = term[0]
    for no in term:
        if no == p_no:
            count += 1
        else:
            n_term.append(str(count))
            n_term.append(p_no)
            count = 1
            p_no = no
    n_term.append(str(count))
    n_term.append(no)
    term = n_term

print "".join(term)
