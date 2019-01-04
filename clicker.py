from Tkinter import *
import Tkinter
import _tkinter
from random import *

import random
import time

window = Tk()
window.title("Clicker game")
window.configure(background="white")


clicks = 0
clickpower = 1
idleclicks = 0
autoclickers = 0
factories = 0
clickbaiters = 0
betterclickprice = 50
autoclickerprice = 200
factoryprice = 5000
clickbaitprice = 100000

def plusclicks():
    global clicks
    global clickpower
    clicks += clickpower
    clicklabel.config(text = clicks)

def betterclick():
    global clicks
    global clickpower
    global betterclickprice
    if clicks <= betterclickprice - 1:
        infolabel.config(text="Not Enough Clicks!")
    elif clicks >= betterclickprice:
        clicks -= betterclickprice
        clicklabel.config(text = clicks)
        clickpower += 1
        betterclickprice += 20
        infolabel.config(text = "Better Click Purchased!")
        betterclick.config(text = "Better Click: {} clicks \n Adds 1 clicking power".format(betterclickprice))

def autoclicker():
    global clicks
    global autoclickers
    global autoclickerprice
    if clicks <= autoclickerprice - 1:
        infolabeltext.config(text = "Not Enough Clicks!")
    else:
        clicks -= autoclickerprice
        autoclickerprice += 100
        clicklabel.config(text = clicks)
        infolabel.config(text = "Auto clicker purchased!")
        autoclicky.config(text = 'Auto Clicker: {} clicks \n Gives 1 Click every second'.format(autoclickerprice))
        autoclickers += 1
        autoclick()
        
def autoclick():
    global window
    global clicks
    global autoclickers
    clicks += autoclickers
    window.after(1000, autoclick)
    clicklabel.config(text = clicks)

def factorypurchase():
    global clicks
    global factories
    global factoryprice
    if clicks <= factoryprice - 1:
        infolabel.config(text = "Not Enough Clicks!")
    else:
        clicks -= factoryprice
        factoryprice += 800
        clicklabel.config(text = clicks)
        infolabel.config(text = "Factory purchased!")
        factory.config(text = 'Factory: {} clicks \n Gives 10 Clicks every second'.format(factoryprice))
        factories += 1
        autofactory()

def autofactory():
    global window
    global clicks
    global factories
    clicks += factories * 10
    window.after(1000, autofactory)
    clicklabel.config(text = clicks)

def clickbaitpurchase():
    global clicks
    global clickbaiters
    global clickbaitprice
    if clicks <= clickbaitprice - 1:
        infolabel.config(text = "Not Enough Clicks!")
    else:
        clicks -= clickbaitprice
        clickbaitprice += 9000
        clicklabel.config(text = clicks)
        infolabel.config(text = "Clickbait purchased!")
        clickbait.config(text = 'Clickbait: {} clicks \n Gives 500 Clicks every second'.format(clickbaitprice))
        clickbaiters += 1
        autoclickbait()

def autoclickbait():
    global window
    global clicks
    global clickbaiters
    clicks += clickbaiters * 500
    window.after(1000, autoclickbait)
    clicklabel.config(text = clicks)
    
clickButton = Button(window, text='Click Me', command=plusclicks)
clickButton.grid(row=2, column=0, sticky=W)
clickButton.config(height=5, width=10)
clicklabel = Label(window, text=clicks)
clicklabel.grid(row=1, column=0, sticky=W)
infolabel = Label(window, text="")
infolabel.grid(row=3, column=0)
betterclick = Button(window, text='Better Click: {} clicks \n Adds 1 clicking power'.format(betterclickprice), command=betterclick)
betterclick.grid(row=1, column=6)
autoclicky= Button(window, text='Auto Clicker: {} clicks \n Gives 1 Click every second'.format(autoclickerprice), command=autoclicker)
autoclicky.grid(row=2, column=6)
factory= Button(window, text='Factory: {} clicks \n Gives 10 Clicks every second'.format(factoryprice), command=factorypurchase)
factory.grid(row=3, column=6)
clickbait= Button(window, text='Clickbait: {} clicks \n Gives 500 Clicks every second'.format(clickbaitprice), command=clickbaitpurchase)
clickbait.grid(row=4, column=6)

window.mainloop()