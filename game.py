from tkinter import*
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('800x600-0-0')
c = Canvas (root, bg ='white')
colors = ['red', 'blue', 'green', 'yellow', 'black']
n = 0
ball1 = [0, 0, 0, 0, 0, 0, 0]
ball2 = [0, 0, 0, 0, 0, 0, 0]
ball3 = [0, 0, 0, 0, 0, 0, 0]
balls = [ball1, ball2, ball3]
i = 0
r = 40
v = 10
l1 = Label(width = 20, text = n)

def new_ball ():
	global balls
	c.delete (ALL)
	for i in range (0, 3):
		balls[i][0] = rnd(100, 700)
		balls[i][1] = rnd(100, 500)
		balls[i][2] = rnd(r - 10, r + 10)
		balls[i][3] = rnd (-v, v)
		balls[i][4] = rnd (-v, v)
		balls[i][5] = (c.create_oval(balls[i][0] - balls[i][2], balls[i][1] - balls[i][2], balls[i][0] + balls[i][2], balls[i][1] + balls[i][2], fill = choice(colors), width = 1))
	root.after(3000, new_ball)

	
def click (event):
	global n
	for i in range (0, 3):
		if ((balls[i][0] - event.x)**2 + (balls[i][1] - event.y)**2 <= (1.5*balls[i][2])**2):
			n+= 1
			print(n)
			l1.config(text = n)
			
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

	
def change1 ():
	global i
	i = 1
	
def change2 ():
	global i
	i = 2
	
def change21 ():
	global v, r
	v = 7
	r = 60

def change22 ():
	global v, r
	v = 10
	r = 40

def change23 ():
	global v, r
	v = 13
	r = 20
	
def Prove ():
	global i, j
	if (i == 1):
		c.pack(fill=BOTH, expand=1)
		new_ball()
		move()
		prov()
	elif (i == 2):
		b1 = Button(root, text='Легко', name='btn21', command=change21)
		b2 = Button(root, text='Ноомально', name='btn22', command=change22)
		b3 = Button(root, text='Сложно', name='btn23', command=change23)
		b1.pack()
		b2.pack()
		b3.pack()
		i = 0
		root.after (1, Prove)
	else:
		root.after (1, Prove)
	
def prov ():
	c.bind('<Button-1>', click)
	root.after (1, prov)
	

def wn1():
    lst = root.grid_slaves()
    for l in lst:
        l.destroy()
    root.geometry('512x256')
    root.config(bg='GRAY')
 
b1 = Button(root, text='Начать', name='btn1', command=change1)
#b1.grid(row=0, column=0)
b2 = Button(root, text='Сложность', name='btn2', command=change2)
#b2.grid(row=0, column=0)
l1.pack()
b1.pack()
b2.pack()

Prove()
root.mainloop()


