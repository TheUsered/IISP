from Tkinter import *
import Tkinter
import _tkinter
from random import *
import random
import time
import drop

#new

window = Tk()
window.title("IISP Simulation game")
window.configure(background="black")



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
		def dropm(self, window, button1, b2):
			button_number = button1
			tkvar = StringVar(window)
			
	 
			# Dictionary with options
			choices = { 'House', 'Park', 'Office'}
			tkvar.set('Choose') # set the default option
			
			pop = popupMenu = OptionMenu(window, tkvar, *choices)
			
			choose = Label(window, text="Choose a building", bg="black", fg="white")
			choose.grid(row = 4, column = 0)
			pop.grid(row = 5, column = 0)
			 
			# on change dropdown value
			def change_dropdown(*args):
			    print( tkvar.get() )
			 
			# link function to change dropdown
			tkvar.trace('w', change_dropdown)
			def ok(button_number, oke, pop, choose):
				
   				print "value is", tkvar.get()
				building = tkvar.get()
				
				
				build1(building, button_number, choose, oke, pop, button1, b2, tkvar)
				
			
			
			oke = Button(window, text="OK", command=lambda: ok(button_number, oke, pop, choose))
			
			oke.grid()
		def drop2(self, window, button1, b2):
			button_number = button1
			tkvar2 = StringVar(window)
			
	 
			# Dictionary with options
			choices = { 'House', 'Park', 'Office'}
			tkvar2.set('Choose') # set the default option
			
			pop = popupMenu = OptionMenu(window, tkvar2, *choices)
			
			choose = Label(window, text="Choose a building", bg="black", fg="white")
			choose.grid(row = 4, column = 0)
			pop.grid(row = 5, column = 0)
			 
			# on change dropdown value
			def change_dropdown(*args):
			    print( tkvar2.get() )
			 
			# link function to change dropdown
			tkvar2.trace('w', change_dropdown)
			def ok(button_number, oke, pop, choose):
				
   				print "value is", tkvar2.get()
				building = tkvar2.get()
				
				
				build2(building, button_number, choose, oke, pop, button1, b2, tkvar2)
				
			
			
			oke = Button(window, text="OK", command=lambda: ok(button_number, oke, pop, choose))
			
			oke.grid()


		def destroy(choose, oke, pop):
			choose.destroy()
			oke.destroy()
			pop.destroy()
			
		def destroyb2(b2):
			
			
			b2.destroy()
			

		
				
				
				
				
					
						
				





































		def build1(building, button_number, choose, oke, pop, button1, b2, tkvar):
			print "b1 is happening"
			if building == "House":		
				button1.grid_forget()
				destroy(choose, oke, pop)
				
				b1_2 = Button (window, text="House", bg="black", fg="white", width=10, height=10, state=DISABLED, command=lambda: drop(self, window, button1, b2)) 
				b1_2.grid(row=1, column=0, sticky=W)
				building_out = True
				
				
				#build(building, button_number, choose, oke, pop, button1, b2, tkvar, None)
			if building == "Park":
				
				button1.grid_forget()
				destroy(choose, oke, pop)
				b1_2 = Button (window, text="Park", bg="black", fg="white", width=10, height=10, state=DISABLED, command=lambda: drop(self, window, button1, b2))
				b1_2.grid(row=1, column=0, sticky=W)
				building_out = True
				
				#build(building, button_number, choose, oke, pop, button1, b2, tkvar, None)
				
				
				building = 0
			if building == "Office":
				
				button1.grid_forget()
				destroy(choose, oke, pop)
				b1_2 = Button (window, text="Office", bg="black", fg="white", width=10, height=10, state=DISABLED, command=lambda: drop(self, window, button1, b2)) 
				b1_2.grid(row=1, column=0, sticky=W)
				building_out = True
				
				#build(building, button_number, choose, oke, pop, button1, b2, tkvar, None)
				
				building = 0
		def build2(building, button_number, choose, oke, pop, button1, b2, tkvar2):
			print "bulid 2"
			
			#building = tkvar.get()
			if building == "House":		
				
				destroy(choose, oke, pop)
				destroyb2(b2)
				b2_2 = Button (window, text="House", bg="black", fg="white", width=10, height=10, command=lambda: drop2(self, window, button1, b2)) 
				b2_2.grid(row=1, column=1, sticky=E)
				building_out = True
				
				#build(building, button_number, choose, oke, pop, button1, b2, None, tkvar2)
			if building == "Park":
				
				
				destroy(choose, oke, pop)
				destroyb2(b2)
				b1_2 = Button (window, text="Park", bg="black", fg="white", width=10, height=10, state=DISABLED, command=lambda: drop2(self, window, button1, b2))
				b1_2.grid(row=1, column=1, sticky=E)
				building_out = True
				
				#build(building, button_number, choose, oke, pop, button1, b2, None, tkvar2)
				
				
			if building == "Office":
				
				
				destroy(choose, oke, pop)
				destroyb2(b2)
				b1_2 = Button (window, text="Office", bg="black", fg="white", width=10, height=10, state=DISABLED, command=lambda: drop2(self, window, button1, b2)) 
				b1_2.grid(row=1, column=1, sticky=E)
				building_out = True
				
				#build(building, button_number, choose, oke, pop, button1, b2, None, tkvar)
				
			else:
				pass
		def build3():
			print "build3"
				
		Label (window, text="Welcome to the world", bg="black", fg="white") .grid(row=0, column=0, sticky=S)
		'''
		button1 = Button (window, text="click to add", bg="black", fg="white", width=10, height=10, command=lambda: drop(self, window, button1, b2))
		button1.grid(row=1, column=0, sticky=W)
		b2 = Button (window, text="click to add", bg="black", fg="white", width=10, height=10, command=lambda: drop2(self, window, button1, b2)) 
		b2.grid(row=1, column=1, sticky=W)
		print b2'''
		
		btn=  [[0 for x in xrange(2)] for x in xrange(2)] 
		for x in range(2):
			for y in range(2):
				btn[x][y] = Button(window, text="Choose", width=14, height=5, command= lambda x1=x, y1=y: drop.droper(window, x1, y1))
				btn[x][y].grid(column=x, row=y+1)
				
		'''
		b3 = Button (window, text="click to add", bg="black", fg="white", width=30, command=lambda: click(button1, b2)) 
		b3.grid(row=2, column=0, sticky=W)
		b4 = Button (window, text="click to add", bg="black", fg="white", width=30, command=lambda: click(button1, b2)) 
		b4.grid(row=2, column=1, sticky=W)'''
		
		
	
		



my_gui = alls(window)
window.mainloop()

































