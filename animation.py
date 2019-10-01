from tkinter import *
from graph import *
from math import*
import time
xyz=0
y = 900
Sizex = 1000
Sizey = 1800
canvasSize(Sizex, Sizey)
windowSize(Sizex, Sizey)
def Mishka ():
	c.create_oval (Sizex/10, 600*Sizey/1800, 5*Sizex/10, 1500*Sizey/1800, fill = 'white')
	c.create_oval (28*Sizex/100, 500*Sizey/1800, 5*Sizex/10, 630*Sizey/1800, fill = 'white')
	c.create_oval (38*Sizex/100, 890*Sizey/1800, 6*Sizex/10, 1000*Sizey/1800, fill = 'white')
	c.create_oval (25*Sizex/100, 1270*Sizey/1800, 55*Sizex/100, 1520*Sizey/1800, fill = 'white')
	c.create_oval (35*Sizex/100, 1400*Sizey/1800, 6*Sizex/10, 1520*Sizey/1800, fill = 'white')
	penColor(0, 0, 0)
	brushColor("black")
	c.create_oval (36*Sizex/100,520*Sizey/1800,38*Sizex/100,540*Sizey/1800)
	c.create_oval (49*Sizex/100,530*Sizey/1800,51*Sizex/100,550*Sizey/1800,fill='black')
	brushColor("white")
	c.create_oval (27*Sizex/100,490*Sizey/1800,33*Sizex/100,550*Sizey/1800, fill = 'white')
	penColor("white")
	c.create_oval (272*Sizex/1000,493*Sizey/1800,33*Sizex/100,551*Sizey/1800, fill = 'white')
	
def Solnce ():
	global Sizex, Sizey
	
	brushColor("DeepSkyBlue")
	penColor("lightyellow")
	penSize(20)
	circle (Sizex*7/10, Sizey*5/36, 150)
	penSize(1)
	brushColor("lightyellow")
	circle (Sizex*7/10, Sizey*5/36, 50)
	c.create_oval (550*Sizex/1000,100,850*Sizex/1000,400)
	penSize(1)
	brushColor("lightyellow")
	c.create_oval (650*Sizex/1000,750,850*Sizex/1000,300,fill="lightyellow")
	

'''def Fish (x, y):
	global objp1, objl2, objh3
	
    objp1 = c.create_arc(x, y, x + 500, y + 500,start=143, extent=90, style=ARC, outline='black', width=1,fill="blue")
	objl2 = c.create_arc(x+30, y +300,x +130, y + 450, start=245, extent=50, style=ARC, outline='black', width=1)
	objh3 = c.create_arc(x-353, y + 32, x + 127, y +532, start=47, extent=-90, style=ARC, outline='black', width=1)'''
	
def Fish2 ():
	c.create_arc(400, 1600, 900, 2100, start=53, extent=90, style=ARC, outline='black', width=1)
	c.create_arc(450, 1550,650, 1750, start=155, extent=50, style=ARC, outline='black', width=1)
	c.create_arc(400, 1200, 900, 1700, start=-53, extent=-90, style=ARC, outline='black', width=1)

def Update ():
	global xyz, j, u, y, dy, dx, l
	
	xyz=xyz+0.1
	deleteObject(j)
	deleteObject(u)
#вращается мельница	
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
#
#mouth	
	penColor("black")
	global rot1
	global rot2
	deleteObject(rot1)
	deleteObject(rot2)
	if y<500*Sizey/1800:
		rot1=polygon([(470*Sizex/1000,590*Sizey/1800),(460*Sizex/1000,587*Sizey/1800),(460*Sizex/1000,600*Sizey/1800),(470*Sizex/1000,600*Sizey/1800),(470*Sizex/1000,590*Sizey/1800),
		(470*Sizex/1000,590*Sizey/1800),(450*Sizex/1000,584*Sizey/1800),(450*Sizex/1000,600*Sizey/1800),(470*Sizex/1000,600*Sizey/1800),(470*Sizex/1000,590*Sizey/1800),
		(470*Sizex/1000,590*Sizey/1800),(440*Sizex/1000,581*Sizey/1800),(440*Sizex/1000,600*Sizey/1800),(470*Sizex/1000,600*Sizey/1800),(470*Sizex/1000,590*Sizey/1800),
		(470*Sizex/1000,590*Sizey/1800),(430*Sizex/1000,578*Sizey/1800),(430*Sizex/1000,600*Sizey/1800),(470*Sizex/1000,600*Sizey/1800),(470*Sizex/1000,590*Sizey/1800)])
	else:
		rot2=polygon([(470*Sizex/1000,600*Sizey/1800),(410*Sizex/1000,610*Sizey/1800),(420*Sizex/1000,610*Sizey/1800)])
	penSize(5)
	penColor("red")
#	
	

 
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
brushColor('DeepSkyBlue')
rectangle(0, 0, 1000, 900)
penColor(0, 0, 0)
penSize(10)
polyline([(530, 1010), (700, 600), (900, 400)])
penSize(1)
c.create_oval (650, 1300, 1000, 1550, fill = 'CadetBlue')
c.create_oval (700, 1350, 1000, 1500, fill = 'SteelBlue')

x = 850
dy = -5
dx = 0
objp1 = c.create_arc(x, y, x + 500, y + 500,start=143, extent=90, style=ARC, outline='black', width=1,fill="blue")
objl2 = c.create_arc(x+30, y +300,x +130, y + 450, start=245, extent=50, style=ARC, outline='black', width=1)
objh3 = c.create_arc(x-353, y + 32, x + 127, y +532, start=47, extent=-90, style=ARC, outline='black', width=1)

#Fish(x, y)

l = line(900, 400, 900, 1000)

Mishka()

Fish2()

Solnce()

polyline([(370, 590), (420, 590), (460, 590), (500, 570)])

penColor(255,0,255)
penSize(5)
brushColor("blue")
rectangle(100, 100, 300, 200)
brushColor("yellow")
polygon([(100,100), (200,50), (300,100), (100,100)])

onKey(keyPressed)
onTimer(Update,50)

run()
