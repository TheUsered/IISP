from Tkinter import *
import Tkinter
import _tkinter
from random import *

import random
import time


#new

window = Tk()
window.title("IISP Simulation game")
window.configure(background="black")

house = Tkinter.PhotoImage(file="/home/evan/Documents/IISPImages/Webp.net-resizeimage.gif")

money = 500000
polution = 0
#class house:


def Check(polution):
	if polution >= 101:
		#gameover
		window.destroy()
		window2 = Tk()
		window2.title("GAME OVER")
		window2.configure(background="red")
		lde = Label(window2, bg="red", text="GAME OVER", font="Times 100 bold") .grid()
	else:
		pass

class alls:
	house = Tkinter.PhotoImage(file="/home/evan/Documents/IISPImages/Webp.net-resizeimage.gif")
	LABEL_TEXT = [
	        "Welcome to...",
	        "My IISP game thing",
	        "by...",
	        "Evan",
	      
	    ]
	
	
		
	def __init__(self, window):
		self.window = window

		self.label_index = 0
		self.label_text = StringVar()
		self.label_text.set(self.LABEL_TEXT[self.label_index])
		self.label = Label(window, textvariable=self.label_text, bg="black", fg="white", font="none 50 bold")
		self.label.bind("<Button-1>", self.cycle_label_text)
		self.label.grid(row=2, column = 2, sticky=NE)

	


		
	

	def cycle_label_text(self, event):
        	self.label_index += 1
		building = 1
		if self.label_index >= len(self.LABEL_TEXT):
			self.label.grid_forget()
			self.Map(window, building)
		else:
			pass 
        	self.label_text.set(self.LABEL_TEXT[self.label_index])

	def Map(self, window, building_1):
		


		def destroy(choose, oke, pop):
			choose.destroy()
			oke.destroy()
			pop.destroy()
			
		def droper(window, x1, y1):
			x2 = str(x1)
			y2 = str(y1)
			xy3 = x2 + y2
			
			tkvar = StringVar(window)
			

			# Dictionary with options
			choices = { 'House', 'Park', 'Office', 'Anti-Polution Center'}
			tkvar.set('Choose') # set the default option
			
			pop = popupMenu = OptionMenu(window, tkvar, *choices)
			
			choose = Label(window, text="Choose a building", bg="black", fg="white")
			choose.grid(row = 322, column = 0)
			pop.grid(row = 323, column = 0)
			 
			# on change dropdown value
			def change_dropdown(*args):
				print( tkvar.get() )
			 
			# link function to change dropdown
			tkvar.trace('w', change_dropdown)
			def ok(oke, pop, choose):
				
				print "value is", tkvar.get()
				building = tkvar.get()
				builder(window, x1, y1, building, oke, pop, choose)
				
				
				
				

				
			
			
			oke = Button(window, text="OK", command=lambda: ok(oke, pop, choose))
			
			oke.grid()
			
		def builder(window, x1, y1, building, oke, pop, choose):
			destroy(choose, oke, pop)
			global house
			
			print house
			
			btn[x1][y1].config(text=None)
			btn[x1][y1].config(state=DISABLED)
			btn[x1][y1].config(image=house)
			btn[x1][y1].photo = house
			btn[x1][y1].config(width=100, height=100)
			global polution
			polution = 1000
			Check(polution)
			
				

				
		Label (window, text="Welcome to ", bg="black", fg="white", font="bold 25") .grid(row=0, column=0, sticky=S)
		Label (window, text="the world", bg="black", fg="white", font="bold 25") .grid(row=0, column=1, sticky=S)
		
		
		btn=  [[0 for x in xrange(2)] for x in xrange(2)] 
		for x in range(2):
			for y in range(2):
				btn[x][y] = Button(window, text="Choose", width=14, height=5, command= lambda x1=x, y1=y: droper(window, x1, y1))
				btn[x][y].grid(column=x, row=y+1)
				
		
		
		
	


my_gui = alls(window)
window.mainloop()
