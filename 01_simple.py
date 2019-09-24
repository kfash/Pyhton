# coding: utf-8
"""
Использование графического модуля graph.py.
GR_SIMPLE - простые программы
  (C) К. Поляков, 2017
  e-mail: kpolyakov@mail.ru
  web: http://kpolyakov.spb.ru
"""
from tkinter import *
from graph import *
from math import*
import time
xyz=0
def Fish (x, y):
    c.create_arc(x, y, x + 500, y + 500,start=143, extent=90, style=ARC, outline='black', width=1)
    c.create_arc(x+30, y +300,x +130, y + 450, start=245, extent=50, style=ARC, outline='black', width=1)
    c.create_arc(x-353, y + 32, x + 127, y +532, start=47, extent=-90, style=ARC, outline='black', width=1)

def Update ():
	global xyz
	global j
	global u
	xyz=xyz+0.1
	deleteObject(j)
	deleteObject(u)
	brushColor("lightYellow")
	penColor("lightYellow")
	penSize(1)
	j=polygon([(700+(int)(151*sin(xyz)),250+(int)(151*cos(xyz))),
	(700+(int)(151*sin(xyz+0.3)),250+(int)(151*cos(xyz+0.3))),
	(700+(int)(151*sin(xyz+3.141)),250+(int)(151*cos(xyz+3.141))),
	(700+(int)(151*sin(xyz+3.141+0.3)),250+(int)(151*cos(xyz+3.141+0.3)))])
	
	u=polygon([(700+(int)(151*sin(xyz+1.57)),
	250+(int)(151*cos(xyz+1.57))),(700+(int)(151*sin(xyz+0.3+1.57)),
	250+(int)(151*cos(xyz+0.3+1.57))),(700+(int)(151*sin(xyz+3.141+1.57)),
	250+(int)(151*cos(xyz+3.141+1.57))),(700+(int)(151*sin(xyz+3.141+0.3+1.57)),
	250+(int)(151*cos(xyz+3.141+0.3+1.57)))])
	
	penColor("black")
	global rot1
	global rot2
	deleteObject(rot1)
	deleteObject(rot2)
	if y<500:
		rot1=polygon([(470,590),(460,587),(460,600),(470,600),(470,590),
		(470,590),(450,584),(450,600),(470,600),(470,590),
		(470,590),(440,581),(440,600),(470,600),(470,590),
		(470,590),(430,578),(430,600),(470,600),(470,590)])
	else:
		rot2=polygon([(470,600),(410,610),(420,610)])
	penSize(5)
	penColor("red")
	
	
	global l
	global y
	global dy
	global dx
	moveObjectBy(objp1, dx, dy)
	moveObjectBy(objl2, dx, dy)
	moveObjectBy(objh3, dx, dy)
	deleteObject (l)
	l = line(900, 400, 900, y + 98 + dy)
	y = y + dy
	
	
		
		
	if y >= 1000:
		dy = -dy
	if y <= 380:
		dy = -dy
		 
	
def keyPressed(event):
  if event.keycode == VK_ESCAPE:
    close()  # закрыть окно 
rot1=circle(100,100,100)
rot2=circle(200,100,100)
u=circle(100,100,100)
j=circle(100,100,100)
c = canvas()
c.pack()
canvasSize(1000, 1800)
windowSize(1000, 1800)
brushColor('DeepSkyBlue')
rectangle(0, 0, 1000, 900)
#while True:
penColor(0, 0, 0)
penSize(10)
polyline([(530, 1010), (700, 600), (900, 400)])
penSize(1)
c.create_oval (650, 1300, 1000, 1550, fill = 'CadetBlue')
c.create_oval (700, 1350, 1000, 1500, fill = 'SteelBlue')
#Fish (850, 900)
x = 850
y = 900
dy = -5
dx = 0
objp1 = c.create_arc(x, y, x + 500, y + 500,start=143, extent=90, style=ARC, outline='black', width=1,fill="blue")
objl2 = c.create_arc(x+30, y +300,x +130, y + 450, start=245, extent=50, style=ARC, outline='black', width=1)
objh3 = c.create_arc(x-353, y + 32, x + 127, y +532, start=47, extent=-90, style=ARC, outline='black', width=1)
l = line(900, 400, 900, 1000)
c.create_oval (100, 600, 500, 1500, fill = 'white')
c.create_oval (280, 500, 500, 630, fill = 'white')
c.create_oval (380, 890, 600, 1000, fill = 'white')
c.create_oval (250, 1270, 550, 1520, fill = 'white')
c.create_oval (350, 1400, 600, 1520, fill = 'white')
penColor(0, 0, 0)
brushColor("black")
circle (370, 530, 10)
circle (500, 540, 10)
brushColor("white")
circle (300, 520, 30)
penColor("white")
circle (301, 522, 29)
brushColor("DeepSkyBlue")
penColor("lightyellow")
penSize(20)


circle (700, 250, 150)
penSize(1)
brushColor("lightyellow")
circle (700, 250, 50)



c.create_arc(400, 1600, 900, 2100, start=53, extent=90, style=ARC, outline='black', width=1)
c.create_arc(450, 1550,650, 1750, start=155, extent=50, style=ARC, outline='black', width=1)
c.create_arc(400, 1200, 900, 1700, start=-53, extent=-90, style=ARC, outline='black', width=1)
polyline([(370, 590), (420, 590), (460, 590), (500, 570)])

penColor(255,0,255)
penSize(5)
brushColor("blue")
rectangle(100, 100, 300, 200)
brushColor("yellow")
polygon([(100,100), (200,50), (300,100), (100,100)])

onKey(keyPressed)
onTimer(Update,50)
'''while (True):
    Update(objp1, objl2, objh3, 5, 0)
    time.sleep(0.5)'''
run()
