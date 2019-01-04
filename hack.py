'''from Tkinter import *
import Tkinter
import _tkinter

window = Tk()
window.title("the experiment")
window.configure(background="black")

r = range(0,4)


btn=  [[0 for x in xrange(20)] for x in xrange(20)] 
for x in range(20):
	for y in range(20):
		btn[x][y] = Button(window,command= lambda x1=x, y1=y: color_change(x1,y1))
		btn[x][y].grid(column=x, row=y)

     

def color_change(x,y):
	print x,y
	if x == 3 and y==3:
		drop33()
	if x in r and y in r:
		drop44()

def drop33():
	print "drop"

def drop44():
	print "44"
window.mainloop()'''











'''

n = input ("Number: ")
n = int(n)
br = 0
er = n +9
while n <= er:
	print n
	n += 1
	br += n
print "Total =", br  '''

'''
s = 0
e = 34 + s 
print e'''

'''


fib = [1, 1]
count = 0
re = False
nd = input("How many Numbers do you want?: ")
nd -= 3

if nd == -2:
	print 1
	count = 21
	nd = 0
	re = True
if nd == 0 and re == False:
	print "1 1 2"
else:
	pass  

while count <= nd:
	n = len(fib) - 2
	n2 = len(fib) - 1
	d = int(fib[n])
	d2 = int(fib[n2])
	s = d + d2
	
	fib.append(s)
	
	count += 1
if nd == 0:	
	pass
else:
	print fib'''
'''

w = 10 ** 100

e = [1,]
ed = 0
while ed <= w:
	e.append(0)
	ed += 1

print e
	'''
fib = [1, 1]
count = 0
re = False
nd = input("How many Numbers do you want?: ")


 

while count <= nd:
	s = 01001011101001101101
	d = 1100010110101001
	
	fib.append(s)
	fib.append(d)
	
	count += 1

print fib






