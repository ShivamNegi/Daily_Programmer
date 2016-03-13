from math import sqrt

def factors(no):
	li = []
	for i in xrange(2, int(no/2) ):
		if no % i == 0:
			li.append(i)
	return li

def Isprime(li):
	li_prime = []
	for no in li:
		flag = True
		for i in range(2, int(sqrt(no))+1):
			if no % i == 0:
				flag = False
				break
		if flag:
			li_prime.append(no)
	return li_prime

t = int(raw_input("Enter the number of test cases: "))
for i in range(t):
	tu = raw_input() 
	out = tu
	tu = tu.strip('()')
	tu = tu.split(',')
	num1 = int(tu[0])
	num2 = int(tu[1])
	li_prime1 = Isprime(factors(num1)) 
	li_prime2 = Isprime(factors(num2))
	prod1 = 1
	for no in li_prime1:
		prod1 *= no
	prod2 = 1
	for no in li_prime2:
		prod2 *= no
	if(sum(li_prime2) == sum(li_prime1) and prod2 == num2 and prod1 == num1):
		print out,
		print ' VALID'
	else:
		print out
		print " NOT VALID"


