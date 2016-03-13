'''create a program that will allow you to enter events organizable by hour. 
There must be menu options of some form, and you must be able to easily edit, add,
 and delete events without directly changing the source code.

(note that by menu i dont necessarily mean gui. as long as you can easily access 
	the different options and receive prompts and instructions telling you 
	how to use the program, it will probably be fine)
'''





import operator

class event:
	def __init__(self, hour, event):
		self.hour = hour
		self.event = event
	def display(self):
		print "Hour:",self.hour
		print "Event:",self.event

def deleting():
	hr = int(raw_input("Which event would you like to delete(hour): "))
	for eve in listing:
		if eve.hour == hr:
			listing.remove(eve)
			break

def editing():
	hr = int(raw_input("Which event would you like to edit(by hour): "))
	for eve in listing:
		if eve.hour == hr:
			eve.event = raw_input("What should be the event name?: ")
			break
	else:
		print "Event Not Found."

listing = []


while(True):
	print "What would you like to do?"
	print "\t1.Add Event\n\t2.Edit Event\n\t3.Delete\n\t4.Display\n\t5.Exit"
	x = int(raw_input())
	if x == 1:
		Event = event(int(raw_input("Enter hour: ")), raw_input("Enter event: "))
		listing.append(Event)
	elif x == 2:
		editing()
	elif x == 3:
		deleting()
	elif x == 4:
		listing.sort(key = operator.attrgetter('hour'))
		for eve in listing:
			eve.display()
	else:
		break
	