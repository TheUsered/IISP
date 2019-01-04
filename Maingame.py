from Tkinter import *
import Tkinter
import _tkinter
from random import *

import random
import time


#new

window = Tk()
window.title("IISP Simulation game")
window.configure(background="white")

house = Tkinter.PhotoImage(file="/home/evan/Documents/IISPImages/Webp.net-resizeimage.gif")
park = Tkinter.PhotoImage(file="/home/evan/Downloads/park-clipart-free-30.gif")
office = Tkinter.PhotoImage(file="/home/evan/Downloads/office-building.gif")
anti = Tkinter.PhotoImage(file="/home/evan/Downloads/Solar_Panel_PNG_Clip_Art-2132.gif")
coal = Tkinter.PhotoImage(file="/home/evan/Downloads/coal-power-plant-clipart-1.gif")
money = 500000
polution = 10
energy = 50
housenum = 0
parknum = 0
officenum = 0
antinum = 0
coalnum = 0

#I NEED INCREMENTALNESS

	


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


	def Check():
		global polution
		global energy
		global money 
		def Checkp(polution):
			global polution
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
			global energy
			if energy <= 0:
				#gameover
				window.destroy()
				window2 = Tk()
				window2.title("GAME OVER")
				window2.configure(background="red")
				lde = Label(window2, bg="red", text="GAME OVER", font="Times 100 bold") .grid()
			elif energy >= 101:
				energy = 100
		def Checkm(money):
			global money
			if money <= 0:
				money =0
		Checkm(polution)
		Checke(energy)
		Checkp(money)

	def Map(self, window, building_1):
		global energy
		global polution
		global money
		
		def buildhouse():
			global energy, polution, money
			global housenum
			housenum += 1
			money -= 500
			energy -= 2
			polution += 2
			monlab.config(text=money)
			polab.config(text=polution)
			enlab.config(text=energy)
			lbl11.config(text=housenum)
		def buildpark():
			global energy, polution, money
			global parknum
			parknum += 1
			money -= 1000
			energy -= 2
			polution -= 5
			monlab.config(text=money)
			polab.config(text=polution)
			enlab.config(text=energy)
			lbl21.config(text=parknum)
		def buildoffice():
			global energy, polution, money
			global officenum
			officenum += 1
			money -= 2000
			energy -= 5
			polution += 10
			monlab.config(text=money)
			polab.config(text=polution)
			enlab.config(text=energy)
			lbl31.config(text=officenum)
		def buildanti():
			global energy, polution, money
			global antinum
			antinum += 1
			money -= 5000
			energy -= 5
			polution -= 20
			monlab.config(text=money)
			polab.config(text=polution)
			enlab.config(text=energy)
			lbl41.config(text=antinum)
		def buildcoal():
			coalnum += 1
			def buildcoal1():
				global energy, polution, money
				global coalnum
			
				money -= 500
				energy -= 2
				polution += 2
				monlab.config(text=money)
				polab.config(text=polution)
				enlab.config(text=energy)
				lbl51.config(text=coalnum)
				window.after(1000, buildcoal1)
			

		#Check()
		
			
			
		
			
			
				
		global house
		global office
		global park
		global anti
		global coal
		global housenum, parknum, officenum, antinum, coalnum
		Label(window, text="Energy:", bg="white", fg="black", font="bold 10") .grid(row=1, column=0, sticky=S)
		Label(window, text="Polution:", bg="white", fg="black", font="bold 10") .grid(row=1, column=1, sticky=S)
		Label(window, text="Money:", bg="white", fg="black", font="bold 10") .grid(row=1, column=2, sticky=S)
		enlab = Label(window, text=energy, bg="white", fg="black", font="bold 10") 
		enlab.grid(row=2, column=0, sticky=S)
		polab = Label(window, text=polution, bg="white", fg="black", font="bold 10") 
		polab.grid(row=2, column=1, sticky=S)
		monlab=Label(window, text=money, bg="white", fg="black", font="bold 10") 
		monlab.grid(row=2, column=2, sticky=S)

		
		#house
		lbl1 = Label(window, image=house) 
		lbl1.grid(row=3, column=0, sticky=S)
		btn1 = Button(window, text="Build House", bg="white", fg="black", font="bold 25", command=buildhouse) 
		btn1.grid(row=3, column=1, sticky=S)
		lbl11 = Label(window, text=housenum) 
		lbl11.grid(row=3, column=2, sticky=S)
		#park
		lbl2 = Label(window, image=park) 
		lbl2.grid(row=4, column=0, sticky=S)
		btn2 = Button(window, text="Build Park", bg="white", fg="black", font="bold 25", command=buildpark) 
		btn2.grid(row=4, column=1, sticky=S)
		lbl21 = Label(window, text=parknum) 
		lbl21.grid(row=4, column=2, sticky=S)
		#office
		lbl3 = Label(window, image=office) 
		lbl3.grid(row=5, column=0, sticky=S)
		btn3 = Button(window, text="Build Office", bg="white", fg="black", font="bold 25", command=buildoffice) 
		btn3.grid(row=5, column=1, sticky=S)
		lbl31 = Label(window, text=officenum) 
		lbl31.grid(row=5, column=2, sticky=S)
		#anti
		lbl4 = Label(window, image=anti) 
		lbl4.grid(row=6, column=0, sticky=S)
		btn4 = Button(window, text="Build Anti Pollution Center", bg="white", fg="black", font="bold 25", command=buildanti) 
		btn4.grid(row=6, column=1, sticky=S)
		lbl41 = Label(window, text=antinum) 
		lbl41.grid(row=6, column=2, sticky=S)
		#coal
		lbl5 = Label(window, image=coal) 
		lbl5.grid(row=7, column=0, sticky=S)
		btn5 = Button(window, text="Build Coal Power Plant", bg="white", fg="black", font="bold 25", command=buildcoal) 
		btn5.grid(row=7, column=1, sticky=S)
		lbl51 = Label(window, text=coalnum) 
		lbl51.grid(row=7, column=2, sticky=S)
		
		
		
	
		



my_gui = alls(window)
window.mainloop()
