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
park = Tkinter.PhotoImage(file="/home/evan/Downloads/park-clipart-free-30.gif")
office = Tkinter.PhotoImage(file="/home/evan/Downloads/office-building.gif")
anti = Tkinter.PhotoImage(file="/home/evan/Downloads/Solar_Panel_PNG_Clip_Art-2132.gif")
road = Tkinter.PhotoImage(file="/home/evan/Downloads/cartoon-highway-clipart-1.gif")
coal = Tkinter.PhotoImage(file="/home/evan/Downloads/coal-power-plant-clipart-1.gif")
money = 500000
polution = 10
energy = 50
#class house:


def Checkp(polution):
	
	if polution >= 101:
		#gameover
		window.destroy()
		window2 = Tk()
		window2.title("GAME OVER")
		window2.configure(background="red")
		lde = Label(window2, bg="red", text="GAME OVER", font="Times 100 bold") .grid()
	elif polution <= 0:
		polution = 0
	else:
		pass
def Checke(energy):
	if energy <= 0:
		#gameover
		window.destroy()
		window2 = Tk()
		window2.title("GAME OVER")
		window2.configure(background="red")
		lde = Label(window2, bg="red", text="GAME OVER", font="Times 100 bold") .grid()
	elif energy >= 101:
		energy = 100


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
			#destroy(choose, oke, pop)
			x2 = str(x1)
			y2 = str(y1)
			xy3 = x2 + y2
			
			tkvar = StringVar(window)
			

			# Dictionary with options
			choices = { 'House', 'Park', 'Office', 'Anti-Polution Center','Road', "Coal Power Plant"}
			tkvar.set('Choose') # set the default option
			
			pop = popupMenu = OptionMenu(window, tkvar, *choices)
			
			choose = Label(window, text="Choose a building", bg="black", fg="white")
			choose.grid(row = 1, column = 323)
			pop.grid(row = 2, column = 323)
			 
			
			def change_dropdown(*args):
				print( tkvar.get() )
			 
			
			tkvar.trace('w', change_dropdown)
			def ok(oke, pop, choose):
				
				
				building = tkvar.get()
				builder(window, x1, y1, building, oke, pop, choose)
				
				
				
				

				
			
			
			oke = Button(window, text="OK", command=lambda: ok(oke, pop, choose))
			
			oke.grid(row = 3, column = 323)
			
		def builder(window, x1, y1, building, oke, pop, choose):
			destroy(choose, oke, pop)
			global money
			global energy
			global polution
			if building.lower() == "house":
				global house
				btn[x1][y1].config(text=None)
				btn[x1][y1].config(state=DISABLED)
				btn[x1][y1].config(image=house)
				btn[x1][y1].photo = house
				btn[x1][y1].config(width=100, height=100)
				money -= 500
				energy -= 2
				polution += 2
				monlab.config(text=money)
				polab.config(text=polution)
				enlab.config(text=energy)
			elif building.lower() == "park":
				global park
				btn[x1][y1].config(text=None)
				btn[x1][y1].config(state=DISABLED)
				btn[x1][y1].config(image=park)
				btn[x1][y1].photo = park
				btn[x1][y1].config(width=100, height=100)
				money -= 1000
				energy -= 2
				polution -= 5
				monlab.config(text=money)
				polab.config(text=polution)
				enlab.config(text=energy)
			elif building.lower() == "office":
				global office
				btn[x1][y1].config(text=None)
				btn[x1][y1].config(state=DISABLED)
				btn[x1][y1].config(image=office)
				btn[x1][y1].photo = office
				btn[x1][y1].config(width=100, height=100)
				money -= 2000
				energy -= 5
				polution += 10
				monlab.config(text=money)
				polab.config(text=polution)
				enlab.config(text=energy)
			elif building.lower() == "anti-polution center":
				global anti
				btn[x1][y1].config(text=None)
				btn[x1][y1].config(state=DISABLED)
				btn[x1][y1].config(image=anti)
				btn[x1][y1].photo = anti
				btn[x1][y1].config(width=100, height=100)
				money -= 5000
				energy -= 5
				polution -= 20
				monlab.config(text=money)
				polab.config(text=polution)
				enlab.config(text=energy)
			elif building.lower() == "road":
				global road
				btn[x1][y1].config(text=None)
				btn[x1][y1].config(state=DISABLED)
				btn[x1][y1].config(image=road)
				btn[x1][y1].photo = road
				btn[x1][y1].config(width=100, height=100)
				money -= 200
				energy -= 5
				polution += 10
				monlab.config(text=money)
				polab.config(text=polution)
				enlab.config(text=energy)
			elif building.lower() == "coal power plant":
				global coal
				btn[x1][y1].config(text=None)
				btn[x1][y1].config(state=DISABLED)
				btn[x1][y1].config(image=coal)
				btn[x1][y1].photo = coal
				btn[x1][y1].config(width=100, height=100)
				money -= 3000
				energy += 30
				polution += 30
				monlab.config(text=money)
				polab.config(text=polution)
				enlab.config(text=energy)
			global polution
			
			Checkp(polution)
			Checke(energy)
			
			
		
			
			
		global energy
		global polution
		global money		
		
		Label (window, text="Welcome to ", bg="black", fg="white", font="bold 25") .grid(row=0, column=0, sticky=S)
		Label (window, text="the world", bg="black", fg="white", font="bold 25") .grid(row=0, column=1, sticky=S)
		Label(window, text="Energy:", bg="black", fg="white", font="bold 10") .grid(row=1, column=0, sticky=S)
		Label(window, text="Polution:", bg="black", fg="white", font="bold 10") .grid(row=1, column=1, sticky=S)
		Label(window, text="Money:", bg="black", fg="white", font="bold 10") .grid(row=1, column=2, sticky=S)
		enlab = Label(window, text=energy, bg="black", fg="white", font="bold 10") 
		enlab.grid(row=2, column=0, sticky=S)
		polab = Label(window, text=polution, bg="black", fg="white", font="bold 10") 
		polab.grid(row=2, column=1, sticky=S)
		monlab=Label(window, text=money, bg="black", fg="white", font="bold 10") 
		monlab.grid(row=2, column=2, sticky=S)

		

		btn=  [[0 for x in xrange(5)] for x in xrange(5)] 
		for x in range(5):
			for y in range(5):
				btn[x][y] = Button(window, text="Choose", width=14, height=4, command= lambda x1=x, y1=y: droper(window, x1, y1))
				btn[x][y].grid(column=x, row=y+3)
				
		
		
		
	
		



my_gui = alls(window)
window.mainloop()
