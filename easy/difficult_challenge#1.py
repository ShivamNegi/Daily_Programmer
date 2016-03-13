def compare(guess,choice):
	if guess >choice:
		return "high"
	elif guess < choice:
		return "low"
	else:
		return "equal"

print """\n\nThis is a role reversal guessing game.
Think of a number between 1-100 (including).
I will try to guess it in the least possible chances. 
Peace.
"""
print "Let's Start!"
from random import randint
choice = randint(1,1000)
print "\n\n", str(choice),"\n\n"
guess = randint(1,1000)
lower = 1
upper = 1000
turns = 0
while True:
	turns += 1
	print guess 
	result = compare(guess,choice)
	if result == "high":
		upper = guess - 1		
	elif result == "low":
		lower = guess + 1
	else:
		break
	guess = randint(lower, upper)

print "The number of turns taken to guess are - ",str(turns)
