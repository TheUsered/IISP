from Tkinter import *
import Tkinter
import _tkinter
from random import *
import random
import time


def droper(window, x1, y1):
	x2 = str(x1)
	y2 = str(y1)
	xy3 = x2 + y2
	print xy3
	tkvar = StringVar(window)
	

	# Dictionary with options
	choices = { 'House', 'Park', 'Office'}
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
		
		
		

		
	
	
	oke = Button(window, text="OK", command=lambda: ok(oke, pop, choose))
	
	oke.grid()
def build(window, x1, y1):
	print "hello"


