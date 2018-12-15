def translator():
	pyg = 'ay'
	#to pig latin
	def spliter():

 	 text = raw_input('Enter (a) word(s): ')
 	 words = text.split()
 	 jword = []
 	   # for each word in the line:
 	 for word in words:

 	   sword = word.lower()
 	   first = sword[0]
 	   new_word = sword + first + pyg
 	   new_word = new_word[1:len(new_word)]
 	   jword.append(new_word)
 	   print " ".join(jword)
    
  
	#from pig latin
	def back_spliter():

	  original = raw_input('Enter (a) Pig Latin word(s): ')
	  words = original.split()
	  jword = []
 	  for word in words:	

	    word = word.lower()
	    first = word[len(word)-3]
 	    new_word = word[0:len(word)-3]
 	    new_word = first + new_word
 	    jword.append(new_word)
	    print " ".join(jword)
	not_done = True
	while not_done:

 	 print "Welcome to the Pig latin translator: "
 	 type = raw_input('Would you like to translate To or From Pig latin?: ')

 	 if type == "To" or type == "to":
 	  spliter()
  	  not_done = False
 	 elif type == "From" or type == "from":
 	   back_spliter()
 	   not_done = False
	 else:
  	   print "Try again"

def timer():
	import time
	e = 1
	if e == 1:
		Year = input('How many years?:')
		if Year.isdigit() == True and Year >= 0:
			Day = input("How many days?:")
			if Day >= 0 and Day.isdigit() == True:
				Hour = input('How many hours?:')
				if Hour >= 0 and Hour.isdigit() == True:
					Minute = input('How many minutes?:')
					if Minute >= 0 and Minute.isdigit() == True:
						Second = input('How many Seconds?:')
						e = e + 1
					else:
						print "No U"
				else: 
					print "No U"	
			else:
				print "No U"
	
		else:
			print "No U"
		
		
		


	Second = Second + Minute * 60 + Hour * 3600 + Day * 86400 + Year * 31557600

	print Second


	while Second > 0:
		time.sleep(1)
		Second = Second - 1
		print Second
	print "Done"

def calculator():
	numa = input("First number:")
	if numa.isdigit() == True:
		op = raw_input("*, /, %, + or -:")
		numb = input("Second number:")
		if numb.isdigit() == True:
			if op == "*":
				print numa * numb
			if op == "/":
				print numa / numb
			if op == "+":
				print numa + numb
			if op == "-":
				print numa - numb
			if op == "%":
				print numa % numb
		else:
			print "failed"

	else:
		print "failed"

def date():
	value = input("hello")
	try:
		value = int(value)
		print "hi"
	except ValueError:
		pass  
#acctual thing
print " "
print " "
print " "
print " "
print " "
print " "
print " "
print " "
print " "
print " "
print " "
print " "
print " "
print " "
print " "
print " "
print " "
print " "
print " "
print " "
print " "
print " "
print " "
print " "
while 1 == 1:
	print "Hello welcome to Chat Bot by Evan and co"
	action = raw_input('Type help for more information:')
	if action == "Help" or action == "help" or action == "h":
		print "Translator / tr --- Pig Latin Translator"
		print "Timer / tm --- Timer"
		print "Calc/ c --- Calculator"
		print "Help / h --- Displays help"

	elif action == "Translator" or action == "translator" or action == "tr":
		translator()
	
	elif action == "Timer" or action == "timer" or action == "tm":
		timer()
	
	elif action == "Calc" or action == "calc" or action == "c":
		calculator()

	elif action == "d":
		date()
	else:
		print "hi"
