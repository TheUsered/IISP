import time
import threading
class char:
	jobif = False
	jobtype = "job0"
	food = 100
	money = 300
	clean = 100
	name = raw_input("What is your name?: ")
	age = input("How old are you")
	'''tt = threading.Timer(60, dirtying,clean)
	tt.start()'''

def MainSt():
	print "You are on Main Street"
	print ""
	print ""
	print "Talk"
	print ""
	print "Shop"
	print ""
	print "Park"
	print ""
	print "Bank"
	print ""
	print "House"
	money = money
	if char.jobif == False:
		print "Get a job"
	else:
		print ""	
	mstaction = raw_input("What would you like to do?:")
	if mstaction.lower() == "talk":
		print "talk"
	elif mstaction.lower() == "shop":
		shop()
	elif mstaction.lower() == "park":
		print "park"
	elif mstaction.lower() == "get a job" or mstaction.lower() == "job":
		print "Your job is a McDonalds worker"	
		jobtype = "job1"
		jobif = True
		Work(money,jobif,clean,age,name,food,jobtype)
	elif mstaction.lower() == "house":
		house(money,jobif,clean,age,name,foodjobtype)
	elif mstaction.lower() == "bank":
		Bank(money,jobif,clean,age,name,food,jobtype)
	else:
		MainSt(money,jobif,clean,age,name,food,jobtype)
def Kitchen(money,jobif,clean,age,name,food):
	print "Deposit"
	print ""
	print "Withdraw"
	print ""
	Kact = raw_input("What Would you like to do")
	if Kant.lower() == "deposit" or Kant.lower() == "dep":
		print "hi"
	elif Kant.lower() == "withdraw" or Kant.lower() == "with":
		print "hi"
	else:
		house(money,jobif,clean,age,name,food)
def Bank(money,jobif,clean,age,name,food,jobtype):
	print "Deposit"
	print ""
	print "Withdraw"
	print ""
	Bact = raw_input("What Would you like to do?:")
	if Back.lower() == "deposit" or Bact.lower() == "dep":
		house(money,jobif,clean,age,name,food,jobtype)
	else:
		house(money,jobif,clean,age,name,food,jobtype)

def LiveRm(money,jobif,clean,age,name,food,jobtype):
	print ""
	print ""
	print ""
	print "You are in the living room"
	print ""
	print "TV"
	print ""
	print "Kitchen"
	print ""
	print ""
	LvRm = raw_input("What do you want to do?:")
	if LvRm.lower() == "kitchen":
		Kitchen(money,jobif,clean,age,name,food)
	elif LvRm.lower() == "tv":
		print "There is nothing on"
		LiveRm(money,jobif,clean,age,name,food,jobtype)
	house(money,jobif,clean,age,name,food,jobtype)
def BedRm(money,jobif,clean,age,name,food,jobtype):
	print "You are in your bedroom"
	print ""
	print "Clean"
	print ""
	print "House"
	BRact = raw_input("What would you like to do?:")
	if BRact.lower() == "clean":
		clean = 100
	elif BRact.lower() == "house":
		house(money,jobif,clean,age,name,food,jobtype)
	else:
		BedRm(money,jobif,clean,age,name,food,jobtype)
def Work(money,jobif,clean,age,name,food,jobtype):
	if jobif == True:
		if money == 500:
			print "New job as a Hair Dresser"
			jobtype = "job2"
		print "working"
		time.sleep(6)
		if jobtype == "job1":
			money = money + 20
			print "Money + 20"
			print money
			MainSt(money,jobif,clean,age,name,food)
		elif jobtype == "job2":
			money = money + 30
			print "Money + 30"
			MainSt(money,jobif,clean,age,name,food)
		else:
			money = money
	else:
		print "No job"

		house(money,clean,age,name,jobif,food)
def house(money,clean,age,name,jobif,food,jobtype):
	if food > 100:
		food = 100
	else:
		food = food
	if clean > 100:
		clean = 100
	else:
		clean = clean
	print " "
	print " "
	print " "
	print " "
	print " "
	print "Money:"
	print money
	print " "
	print "Cleanlyness"
	print clean
	print ""
	print "Food"
	print food
	print " "
	print " "
	print "Main Street"
	print " "
	print "Living Room"
	print " "
	print "Bed Room"
	print " "
	print "Work"
	print " "
	houseact = raw_input("What would you like to do: ")
	if houseact.lower() == "main street" or houseact == "main":
		MainSt(money,jobif,clean,age,name,food,jobtype)
	elif houseact.lower() == "living room" or houseact == "live":
		LiveRm(money,jobif,clean,age,name,food,jobtype)
	elif houseact.lower() == "bed room" or houseact == "bed":
		BedRm(money,jobif,clean,age,name,food,jobtype)
	elif houseact.lower() == "work":
		Work(money,jobif,clean,age,name,food,jobtype)
	else:
		print ""
		print ""
		print ""
		print ""
		print ""
		house(money,clean,age,name,jobif,food)
def shop(money,jobif,clean,age,name,food,jobtype):
	print "Welcome to the shop"
	house(money,jobif,clean,age,name,food,jobtype)
def mainmenu(age,name):
	jobif = False
	year = input("How many seconds are in a in game year? ")
	t = threading.Timer(year, ageing,age)
	t.start()
	print ""
	print ""
	print ""
	print ""
	print "You are in your house"
	jobtype = "job0"
	food = 100
	money = 300
	clean = 100
	tt = threading.Timer(60, dirtying,clean)
	tt.start()
	
	
	house(money,clean,age,name,jobif,food,jobtype)

def customize():
	print "Customize your character:"
	name = raw_input("What is your name:")
	age = input("How old are you:")
	cont = raw_input("Customize more? y/n:")
	if cont == "y":
		hair = raw_input("What colour is your hair")
		
	else:
		print "Done"
		print ""
		print ""
		print ""
		print ""
		print ""
		mainmenu(age,name)
		
def dirtying(clean):
	clean = clean - 1
def ageing(age):
	age = age + 1
	print age
def start():
	
	customize()
	
start()
