string = raw_input()
rev = string[::-1]
n = len(string)
if string == rev:
    print "Palindrome."
else:
    print "Not Palindrome."
