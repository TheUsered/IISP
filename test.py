import sys

def admin():
	print "why did I do this"
def action(cre):
	print "action"

cre = False
def actiond(cre):
	action = raw_input("What would you like to do?: ")
	if action.lower() == "admin" and cre == True:
		admin()
	else:
		pass


def creator():
	print "Unlocking system..."
	passw = raw_input("What is the password?: ")
	if passw == "   ":
		pass
	else:
		
		print "Not correct"
		sys.exit()
		
	cre = True
	print "System unlocked"
	actiond(cre)
	



print "Hello my name is jeff"
name = raw_input("What is your name?: ")

if name.lower() == "evan":
	print "Hello Creator"
	creator()
	
else:
	print "Hello", name
	action(cre)





