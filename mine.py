from Tkinter import *
import Tkinter
import _tkinter
from random import *
import random

window = Tk()
window.title("MINE SWEEPER")
window.configure(background="black")
derb = 0
def color(x1,y1):
	print "hi"
	btn[x1][y1].config(bg="red", fg="red", state=DISABLED)

	
	
	
btn=  [[0 for x in xrange(20)] for x in xrange(20)] 
for x in range(20):
	for y in range(20):
		btn[x][y] = Button(window,fg="grey", command= lambda x1=x, y1=y: color(x1,y1))
		btn[x][y].grid(column=x, row=y)




mines = [randint(0, 20),randint(0, 20),randint(0, 20),randint(0, 20),randint(0, 20),randint(0, 20),randint(0, 20),randint(0, 20),randint(0, 20),randint(0, 20)]
minesd = [randint(0, 20),randint(0, 20),randint(0, 20),randint(0, 20),randint(0, 20),randint(0, 20),randint(0, 20),randint(0, 20),randint(0, 20),randint(0, 20)]

'''m1 = mines[0],minesd[0]
m2 = mines[1],minesd[1]
m3 = mines[2],minesd[2]
m4 = mines[3],minesd[3]
m5 = mines[4],minesd[4]
m6 = mines[5],minesd[5]
m7 = mines[6],minesd[6]
m8 = mines[7],minesd[7]
m9 = mines[8],minesd[8]
m10 = mines[9],minesd[9]'''




window.mainloop()

