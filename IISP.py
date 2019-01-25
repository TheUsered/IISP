from Tkinter import *
import Tkinter
import _tkinter
from random import *

import random
import time


#new

window = Tk()
window.title("IISP Simulation game")
window.configure(background="#006600")

house = Tkinter.PhotoImage(file="/home/evan/Downloads/house.gif")
park = Tkinter.PhotoImage(file="/home/evan/Downloads/335950.gif")
office = Tkinter.PhotoImage(file="/home/evan/Downloads/office.gif")
anti = Tkinter.PhotoImage(file="/home/evan/Downloads/1621975.gif")
road = Tkinter.PhotoImage(file="/home/evan/Downloads/cartoon-highway-clipart-1.gif")
coal = Tkinter.PhotoImage(file="/home/evan/Downloads/coal-power-plant-clipart-1.gif")
money = 500000
polution = 0
energy = 100


def Check():
	global money
	global polution
	global energy
	def end():
		#gameover
		window.destroy()
		window2 = Tk()
		window2.title("GAME OVER")
		window2.configure(background="red")
		lde = Label(window2, bg="red", text="GAME OVER", font="Times 100 bold") .grid()
	if polution >= 101:
		end()
		print ""
		print "You had too much pollution"
		print ""
	elif polution <= 0:
		polution = 0

	elif energy <= 0:
		end()
		print ""
		print "You lost all energy"
		print ""	
	elif energy >= 101:
		energy = 100
	elif money <= 0:
		end()
		print ""
		print "You went bankrupt"
		print ""
	else:
		pass
	


class alls:
	
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

		def building_window(x1,y1):


			window3 = Tk()
			window3.title("Building menu")
			window3.configure(background="orange")
			def building_window_destroy(inpute):
				building = inpute
				print building
				builder(window, x1, y1, building)
				window3.destroy()
				


			Label(window3, text="Choose a ", font="bold 25", fg="black", bg="orange").grid(row=0, column=0, sticky=N)
			Label(window3, text="building", font="bold 25", fg="black", bg="orange").grid(row=0, column=1, sticky=N)

			Button(window3, text="House", font="bold 20", fg="black", bg="orange", height=5, command=lambda: building_window_destroy("house")).grid(row=1, column=0, sticky=W)
			Label(window3, text="Simple House, $500", font="bold 10", fg="black", bg="orange").grid(row=1, column=0, sticky=S)
			Button(window3, text="Park", font="bold 20", fg="black", bg="orange", height=5, command=lambda: building_window_destroy("park")).grid(row=1, column=1, sticky=W)
			Label(window3, text="Lowers polutition, $1000", font="bold 10", fg="black", bg="orange").grid(row=1, column=1, sticky=S)
			Button(window3, text="Office", font="bold 20", fg="black", bg="orange", height=5, command=lambda: building_window_destroy("office")).grid(row=1, column=2, sticky=W)
			Label(window3, text="Makes money, $2000", font="bold 10", fg="black", bg="orange").grid(row=1, column=2, sticky=S)
			Button(window3, text="Anti-polution center", font="bold 20", fg="black", bg="orange", height=5, command=lambda: building_window_destroy("anti")).grid(row=1, column=3, sticky=W)
			Label(window3, text="Lowers polution, makes energy, $5000", font="bold 10", fg="black", bg="orange").grid(row=1, column=3, sticky=S)
			Button(window3, text="Road", font="bold 20", fg="black", bg="orange", height=5, command=lambda: building_window_destroy("road")).grid(row=1, column=4, sticky=W)
			Label(window3, text="Just a road, $200", font="bold 10", fg="black", bg="orange").grid(row=1, column=4, sticky=S)
			Button(window3, text="Coal power-plant", font="bold 20", fg="black", bg="orange", height=5, command=lambda: building_window_destroy("coal")).grid(row=1, column=5, sticky=W)
			Label(window3, text="A lot of pollution but a lot of energy, $500", font="bold 10", fg="black", bg="orange").grid(row=1, column=5, sticky=S)


		def upgrade_window(x1,y1):
			window3 = Tk()
			window3.title("Upgrade menu")
			window3.configure(background="orange")
			def building_window_destroy(inpute):
				building = inpute
				print building
				builder(window, x1, y1, building)
				window3.destroy()
			Label(window3, text="Choose a ", font="bold 25", fg="black", bg="orange").grid(row=0, column=0, sticky=N)
			Label(window3, text="Upgrade", font="bold 25", fg="black", bg="orange").grid(row=0, column=1, sticky=N)

			Button(window3, text="House", font="bold 20", fg="black", bg="orange", height=5, command=lambda: building_window_destroy("house")).grid(row=1, column=0, sticky=W)
			Label(window3, text="Simple House, $500", font="bold 10", fg="black", bg="orange").grid(row=1, column=0, sticky=S)
			Button(window3, text="Park", font="bold 20", fg="black", bg="orange", height=5, command=lambda: building_window_destroy("park")).grid(row=1, column=1, sticky=W)
			Label(window3, text="Lowers polutition, $1000", font="bold 10", fg="black", bg="orange").grid(row=1, column=1, sticky=S)
			Button(window3, text="Office", font="bold 20", fg="black", bg="orange", height=5, command=lambda: building_window_destroy("office")).grid(row=1, column=2, sticky=W)
			Label(window3, text="Makes money, $2000", font="bold 10", fg="black", bg="orange").grid(row=1, column=2, sticky=S)
			Button(window3, text="Anti-polution center", font="bold 20", fg="black", bg="orange", height=5, command=lambda: building_window_destroy("anti")).grid(row=1, column=3, sticky=W)
			Label(window3, text="Lowers polution, makes energy, $5000", font="bold 10", fg="black", bg="orange").grid(row=1, column=3, sticky=S)
			Button(window3, text="Road", font="bold 20", fg="black", bg="orange", height=5, command=lambda: building_window_destroy("road")).grid(row=1, column=4, sticky=W)
			Label(window3, text="Just a road, $200", font="bold 10", fg="black", bg="orange").grid(row=1, column=4, sticky=S)
			Button(window3, text="Coal power-plant", font="bold 20", fg="black", bg="orange", height=5, command=lambda: building_window_destroy("coal")).grid(row=1, column=5, sticky=W)
			Label(window3, text="A lot of pollution but a lot of energy, $500", font="bold 10", fg="black", bg="orange").grid(row=1, column=5, sticky=S)



		


		def update(building):
			global money, polution, energy
			
			if building.lower() == "house":
				energy -= 1
				polution += 1
			elif building.lower() == "park":
				polution -= 1
			elif building.lower() == "office":
				energy -= 2
				polution += 1
				money += 1
			elif building.lower() == "anti":
				energy += 2
				polution -= 2
			elif building.lower() == "road":
				polution += 1
			elif building.lower() == "coal":
				energy += 3
				polution += 3
			else:
				print "But how can this be?!?!"
			polab.config(text=polution)
			enlab.config(text=energy)
			monlab.config(text=money)
			Check()
			window.after(1000, lambda: update(building))
			
			
		def builder(window, x1, y1, building):

			global money, energy, polution, house, park, office, anti, roal, coal
			if building.lower() == "house":
				btn[x1][y1].config(image=house)
				btn[x1][y1].photo = house
				money -= 500
			elif building.lower() == "park":
				btn[x1][y1].config(image=park)
				btn[x1][y1].photo = park
				money -= 1000
			elif building.lower() == "office":
				btn[x1][y1].config(image=office)
				btn[x1][y1].photo = office
				money -= 2000
			elif building.lower() == "anti":
				btn[x1][y1].config(image=anti)
				btn[x1][y1].photo = anti
				money -= 5000
			elif building.lower() == "road":
				btn[x1][y1].config(image=road)
				btn[x1][y1].photo = road
				money -= 200
			elif building.lower() == "coal":
				btn[x1][y1].config(image=coal)
				btn[x1][y1].photo = coal
				money -= 3000

			btn[x1][y1].config(text=None)
			btn[x1][y1].config(command=lambda: upgrade_window(x1,y1))
			btn[x1][y1].config(width=100, height=100)
			monlab.config(text=money)
			update(building)
			Check()
			
			
			
		
			
			
		global energy, polution, money
		
		
		Label(window, text="Energy:", bg="#006600", fg="white", font="bold 10") .grid(row=1, column=0, sticky=S)
		Label(window, text="Polution:", bg="#006600", fg="white", font="bold 10") .grid(row=1, column=1, sticky=S)
		Label(window, text="Money:", bg="#006600", fg="white", font="bold 10") .grid(row=1, column=2, sticky=S)
		enlab = Label(window, text=energy, bg="#006600", fg="white", font="bold 10") 
		enlab.grid(row=2, column=0, sticky=S)
		polab = Label(window, text=polution, bg="#006600", fg="white", font="bold 10") 
		polab.grid(row=2, column=1, sticky=S)
		monlab=Label(window, text=money, bg="#006600", fg="white", font="bold 10") 
		monlab.grid(row=2, column=2, sticky=S)

		

		btn=  [[0 for x in xrange(5)] for x in xrange(5)] 
		for x in range(5):
			for y in range(5):
				btn[x][y] = Button(window, text="Choose", fg="white", bg="#006600", relief=FLAT, width=14, height=4, command= lambda x1=x, y1=y: building_window(x1,y1))
				btn[x][y].grid(column=x, row=y+3)
				
		
		
		
	
		



my_gui = alls(window)
window.mainloop()
