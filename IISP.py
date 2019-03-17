from Tkinter import *
import Tkinter
import _tkinter
from random import *

import random
import time
import threading


#new

window = Tk()
window.title("IISP Simulation game")
window.configure(background="#006600")

monlab = None
money = 500000

polab = None
pollution = 0

enlab = None
energy = 100

size = 5
btn =  [[0 for x in xrange(size)] for x in xrange(size)] 

class Property:
    label = ""
    image = None

    def updater(self):
        pass

class House(Property): 
    label = "House"
    image = Tkinter.PhotoImage(file="images/house.gif")
    def updater(self):
        global money, pollution, energy
        energy -= 1
        pollution += 1
        print "Updating "+self.label

    def __init__(self):
        global money
	money -= 500

class Park(Property):
    label = "Park"
    image = Tkinter.PhotoImage(file="images/335950.gif")
    def updater(self):
        global money, pollution, energy
        pollution -= 1
        print "Updating "+self.label

    def __init__(self):
        global money
	money -= 1000

class Office(Property):
    label = "Office"
    image = Tkinter.PhotoImage(file="images/office.gif")
    def updater(self):
        global money, pollution, energy
        energy -= 2
        pollution += 1
        money += 1
        print "Updating "+self.label

    def __init__(self):
        global money
	money -= 2000

class Anti(Property):
    label = "Anti-pollution Centre"
    image = Tkinter.PhotoImage(file="images/1621975.gif")
    def updater(self):
        global money, pollution, energy
        energy += 2
        pollution -= 2
        print "Updating "+self.label

    def __init__(self):
        global money
	money -= 5000

class Road(Property):
    label = "Road"
    image = Tkinter.PhotoImage(file="images/cartoon-highway-clipart-1.gif")
    def updater(self):
        global money, pollution, energy
        pollution += 1
        print "Updating "+self.label

    def __init__(self):
        global money
	money -= 200

class Coal(Property):
    label = "Coal Power Plant" 
    image = Tkinter.PhotoImage(file="images/coal-power-plant-clipart-1.gif")
    def updater(self):
        global money, pollution, energy
        energy += 3
        pollution += 3
        print "Updating "+self.label

    def __init__(self):
        global money
	money -= 3000

class Putton:
    button = None
    property = None
    def __init__(self, x, y, droper, property):
        self.button = Button(window, text="Choose", fg="white", bg="#006600", relief=FLAT, width=14, height=4, command= lambda x1=x, y1=y: droper(window,x1,y1))
        self.property = property

class Checker:
    def __init__(self, interval=1):
        self.interval = interval

        self.checking = True
        self.thread = threading.Thread(target=self.check, args=())
        self.thread.start()

    def end(self):
	#gameover
        print "Game over"
	window3 = Tk()
	window3.title("GAME OVER")
	window3.configure(background="red")
	lde = Label(window3, bg="red", text="GAME OVER", font="Times 100 bold") .grid()
	window3.mainloop()
        self.checking = False;

    def check(self):
	global money, pollution, energy, monlab, enlab, polab
        while self.checking:
            print "In check"
            for x in range(size):
		for y in range(size):
                    btn[x][y].property.updater()

            polab.config(text=pollution)
            enlab.config(text=energy)
            monlab.config(text=money)

            if pollution >= 101:
		print ""
		print "You had too much pollution"
		print ""
		self.end()
	    elif pollution <= 0:
		pollution = 0

	    elif energy <= 0:
		print ""
		print "You lost all energy"
		print ""	
		self.end()
	    elif energy >= 101:
		energy = 100
            elif money <= 0:
		print ""
		print "You went bankrupt"
		print ""
		self.end()
	    else:
		pass
	

            time.sleep(self.interval)

	window.quit()

class alls:
	
	def __init__(self, window):
		self.window = window
		self.Map(window)

	def Map(self, window):

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
			choices = { House.label, Park.label, Office.label, Anti.label, Road.label, Coal.label }
			tkvar.set('Choose') # set the default option
			
			pop = popupMenu = OptionMenu(window, tkvar, *choices)
			
			choose = Label(window, text="Choose a building", bg="#006600", fg="white")
			choose.grid(row = 1, column = 323)
			pop.grid(row = 2, column = 323)
			 
			
			def change_dropdown(*args):
				print( tkvar.get() )
			 
			
			tkvar.trace('w', change_dropdown)
			def ok(oke, pop, choose):

				choose.destroy()
				oke.destroy()
				pop.destroy()				

				building = tkvar.get()
				builder(window, x1, y1, building)

			
			oke = Button(window, text="OK", command=lambda: ok(oke, pop, choose))
			
			oke.grid(row = 3, column = 323)

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

			Button(window3, text=House.label, font="bold 20", fg="black", bg="orange", height=5, command=lambda: building_window_destroy(House.label)).grid(row=1, column=0, sticky=W)
			Label(window3, text="Simple House, $500", font="bold 10", fg="black", bg="orange").grid(row=1, column=0, sticky=S)
			Button(window3, text=Park.label, font="bold 20", fg="black", bg="orange", height=5, command=lambda: building_window_destroy(Park.label)).grid(row=1, column=1, sticky=W)
			Label(window3, text="Lowers polutition, $1000", font="bold 10", fg="black", bg="orange").grid(row=1, column=1, sticky=S)
			Button(window3, text=Office.label, font="bold 20", fg="black", bg="orange", height=5, command=lambda: building_window_destroy(Office.label)).grid(row=1, column=2, sticky=W)
			Label(window3, text="Makes money, $2000", font="bold 10", fg="black", bg="orange").grid(row=1, column=2, sticky=S)
			Button(window3, text=Anti.label, font="bold 20", fg="black", bg="orange", height=5, command=lambda: building_window_destroy(Anti.label)).grid(row=1, column=3, sticky=W)
			Label(window3, text="Lowers pollution, makes energy, $5000", font="bold 10", fg="black", bg="orange").grid(row=1, column=3, sticky=S)
			Button(window3, text=Road.label, font="bold 20", fg="black", bg="orange", height=5, command=lambda: building_window_destroy(Road.label)).grid(row=1, column=4, sticky=W)
			Label(window3, text="Just a road, $200", font="bold 10", fg="black", bg="orange").grid(row=1, column=4, sticky=S)
			Button(window3, text=Coal.label, font="bold 20", fg="black", bg="orange", height=5, command=lambda: building_window_destroy(Coal.label)).grid(row=1, column=5, sticky=W)
			Label(window3, text="A lot of pollution but a lot of energy, $500", font="bold 10", fg="black", bg="orange").grid(row=1, column=5, sticky=S)



		


		def builder(window, x1, y1, building):
			w = 100
			h = 100
                        b = None
			global money, energy, pollution, house, park, office, anti, roal, coal
			btn[x1][y1].button.config(command=lambda: upgrade_window(x1,y1))
			if building == House.label:
                                b = House()
			elif building == Park.label:
                                b = Park()
			elif building == Office.label:
                                b = Office()
			elif building == Anti.label:
                                b = Anti()
			elif building == Road.label:
                                b = Road()
			elif building == Coal.label:
                                b = Coal()
			else:
				w = 14
				h = 4
				btn[x1][y1].button.config(command=lambda: droper(window, x1, y1))

                        if b != None:
                                image =b.image
				btn[x1][y1].button.config(image = image)
				btn[x1][y1].button.photo = image
                                btn[x1][y1].property = b

			btn[x1][y1].button.config(text=None)
			
			btn[x1][y1].button.config(width=w, height=h)
			monlab.config(text=money)
			
			
	        global money, pollution, energy, monlab, enlab, polab
		
		
		Label(window, text="Energy:", bg="#006600", fg="white", font="bold 10") .grid(row=1, column=0, sticky=S)
		Label(window, text="Polution:", bg="#006600", fg="white", font="bold 10") .grid(row=1, column=1, sticky=S)
		Label(window, text="Money:", bg="#006600", fg="white", font="bold 10") .grid(row=1, column=2, sticky=S)
		enlab = Label(window, text=energy, bg="#006600", fg="white", font="bold 10") 
		enlab.grid(row=2, column=0, sticky=S)
		polab = Label(window, text=pollution, bg="#006600", fg="white", font="bold 10") 
		polab.grid(row=2, column=1, sticky=S)
		monlab=Label(window, text=money, bg="#006600", fg="white", font="bold 10") 
		monlab.grid(row=2, column=2, sticky=S)

		
		for x in range(size):
			for y in range(size):
				btn[x][y] = Putton(x, y, droper, Property())
				btn[x][y].button.grid(column=x, row=y+3)
				
		
		
		
	
		



my_gui = alls(window)
checker = Checker()
window.mainloop()
