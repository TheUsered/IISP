import time
'''
print ""
print "______________________________________________________________________________________________________________________________________"
print "|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|"
print "|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|"
print "|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|"
print "|        |         |         |           |          |        |        |         |          |          |          |         |          |"
print "|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|"
print "|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|"
print "|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|"
print "|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|"
print "|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|"
print "|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>+++++++++++++++++++++++++>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|"
print "|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|"
print "|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|"
print "|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|"
print "|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|"
print "|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|"
print "|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>|"
print "||"
print "||"
print "||"
print "||"
print "||"
print "||"
print "||"
print "||"
print "||"
print "||"
print "||"
print "||"
print "||"
print "||"
print "||"
print "|__________________________________s___________________________________________________________________________________________________|"
time.sleep(200)'''










from Tkinter import *
import Tkinter
import _tkinter
from random import *
import random

'''
class Application(Master):
    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "exit"
        self.QUIT["fg"]   = "blue"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "top"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()

class MyFirstGUI:
    LABEL_TEXT = [
        "This is our first GUI!",
        "Actually, this is our second GUI.",
        "We made it more interesting...",
        "...by making this label interactive.",
        "Go on, click on it again.",
    ]
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label_index = 0
        self.label_text = StringVar()
        self.label_text.set(self.LABEL_TEXT[self.label_index])
        self.label = Label(master, textvariable=self.label_text)
        self.label.bind("<Button-1>", self.cycle_label_text)
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

    def cycle_label_text(self, event):
        self.label_index += 1
        self.label_index %= len(self.LABEL_TEXT) # wrap around
        self.label_text.set(self.LABEL_TEXT[self.label_index])

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()


class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Calc")

        self.total = 0
        self.entered_number = 0

        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="Total:")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)

        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.reset_button.grid(row=2, column=2, sticky=W+E)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else: # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

root = Tk()
my_gui = Calculator(root)
root.mainloop()

#key
def click():
	entered_text=textentry.get()
	output.delete(0.0, END)
	try:
		definition= my_compdictionary[entered_text]
	except:
		definition = "sorry"
	output.insert(END, definition)

### Main
Window = Tk()
Window.title("The test")
Window.configure(background="blue")

###Pohto

Label (Window, text="hello", bg="blue") .grid(row=0, column=0, sticky=W)

#label
Label (Window, text="Enter the word:", bg="blue", fg="black", font="none 12 bold") .grid(row=1, column=0, sticky=W)
Label (Window, text="\nDefinition:", bg="blue", fg="black", font="none 12 bold") .grid(row=4, column=0, sticky=W)
#text
textentry = Entry(Window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)
#submit
Button(Window, text="SUBMIT", width=32, command=click) .grid(row=32, column=0, stick=W)
#text box
output = Text(Window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)

#info
def close_window():
	Window.destroy()
	exit()

my_compdictionary = {
	'algorithm': 'step by step', 'bug': 'death'
	}

Label (Window, text="Exit:", bg="blue", fg="white", font="times 12 bold") .grid(row=6, column=0, sticky=W)
Button(Window, text="Exit", width=18, command=close_window) .grid(row=7, column=0, stick=W)

Window.mainloop()

'''
'''
#new
window = Tk()
window.title("the experiment")
window.configure(background="black")

def extra():
	print "extra"

for x in range(60):
	for y in range(20):
		button[x][y] = Button(window,command= lambda: self.extra())
		button[x][y].grid(column=x, row=y)'''



'''
def close_window():
	window.destroy()
	exit()

b1 = tk.Button(window, text="The", bg="black", fg="white", font="Times 12 bold") 
b1.grid(row=6, column = 1, sticky=tk.W)


tk.Button(window, text="The", bg="black", fg="white", font="Times 12 bold") .grid(row=6, column = 3, sticky=E)
tk.Button(window, text="The", bg="black", fg="white", font="Times 12 bold") .grid(row=6, column = 5, sticky=N)
tk.Button(window, text="EXIT", width=6, command=close_window) .grid(row=7, column=6, stick=E)
tk.Label (window, text="                             ", bg="black", fg="white", font="Times 12 bold") .grid(row=6, column = 2, sticky=N)
tk.Label (window, text="                             ", bg="black", fg="white", font="Times 12 bold") .grid(row=6, column = 4, sticky=N)

for x in range(10):
  print random.randint(1,101)

print b1

b1["text"] = "HEY"
'''

#window.mainloop()

#
numb = 1
m = 500
n = 1
while numb <= 13:
	if n == 500:
		n = 0
	else:
		pass
	n += 1
	r = m % n
	if r == 0:
		s = 0
	else:
		s = n % r

	if s == 0:
		t = 0
	else:
		t = r % s
	rrange = range(1,16)
	srange = range(2, 10)
	if r in rrange and s in srange and t == 0:
		print n
		numb += 1
	else:
		pass











	
	
	



