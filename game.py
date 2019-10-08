from tkinter import*
from random import randrange as rnd, choice
import time

root = Tk()
#root.geometry('800x600-0-0')
c = Canvas (root, bg ='white')
colors = ['red', 'blue', 'green', 'yellow', 'black']
n = 0
ball1 = [0, 0, 0, 0, 0, 0, 0]
ball2 = [0, 0, 0, 0, 0, 0, 0]
ball3 = [0, 0, 0, 0, 0, 0, 0]
balls = [ball1, ball2, ball3]
i = 0

def new_ball ():
	global balls
	c.delete (ALL)
	for i in range (0, 3):
		balls[i][0] = rnd(100, 700)
		balls[i][1] = rnd(100, 500)
		balls[i][2] = rnd(30, 50)
		balls[i][3] = rnd (-10, 10)
		balls[i][4] = rnd (-10, 10)
		balls[i][5] = (c.create_oval(balls[i][0] - balls[i][2], balls[i][1] - balls[i][2], balls[i][0] + balls[i][2], balls[i][1] + balls[i][2], fill = choice(colors), width = 1))
	root.after(3000, new_ball)

	
def click (event):
	global n
	for i in range (0, 3):
		if ((balls[i][0] - event.x)**2 + (balls[i][1] - event.y)**2 <= (1.5*balls[i][2])**2):
			n+= 1
			print(n)
			
def move ():
	global balls
	for i in range (0, 3):
		c.move (balls[i][5], balls[i][3], balls[i][4])
		
		if ((c.coords(balls[i][5])[0] < 0) or (c.coords(balls[i][5])[2] > 800)):
			balls[i][3]  = -balls[i][3]
		
		if ((c.coords(balls[i][5])[3] > 600) or (c.coords(balls[i][5])[1] < 0)):
			balls[i][4] = -balls[i][4]
			
			
		balls[i][0] = c.coords(balls[i][5])[0] + balls[i][3]
		balls[i][1] = c.coords(balls[i][5])[1] + balls[i][3]
	
		#print (i)
	root.after (10, move)
	
	b
	
def change ():
	i = 1
	
def Prove ():
	if (i == 1):
		c.pack(fill=BOTH, expand=1)
		new_ball()
		move()
		prov()
	else:
		root.after (1, prov)
	
def prov ():
	c.bind('<Button-1>', click)
	root.after (1, prov)
		

e = Entry (width = 20)
b1 = Button (root, text = " Начать")
e.pack()
b1.pack()
b1.bind('<Button-1>', change)

Prove()
root.mainloop()

