from tkinter import *
from graph import *
from math import*
import time
xyz=0
c = canvas()
c.pack()
Sizex = 500
Sizey = 900
y = Sizey*900/1800
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
	brushColor("DeepSkyBlue")
	penColor("lightyellow")
	penSize(20)
	c.create_oval (Sizex*550/1000, Sizey*100/1800, Sizex*850/1000, Sizey*400/1800, outline ='lightyellow', width = 20)
	penSize(1)
	brushColor("lightyellow")
	c.create_oval (Sizex*650/1000, Sizey*200/1800, Sizex*750/1000, Sizey*300/1800, fill = "lightyellow", outline = "lightyellow", width = 20)

'''def Fish (x, y):
	global objp1, objl2, objh3
	
    objp1 = c.create_arc(x, y, x + 500, y + 500,start=143, extent=90, style=ARC, outline='black', width=1,fill="blue")
	objl2 = c.create_arc(x+30, y +300,x +130, y + 450, start=245, extent=50, style=ARC, outline='black', width=1)
	objh3 = c.create_arc(x-353, y + 32, x + 127, y +532, start=47, extent=-90, style=ARC, outline='black', width=1)'''
	
def Fish2 ():
	c.create_arc(Sizex*400/1000, Sizey*1600/1800, Sizex*900/1000, Sizey*2100/1800, start=53, extent=90, style=ARC, outline='black', width=1)
	c.create_arc(Sizex*450/1000, Sizey*1550/1800, Sizex*650/1000, Sizey*1750/1800, start=155, extent=50, style=ARC, outline='black', width=1)
	c.create_arc(Sizex*400/1000, Sizey*1200/1800, Sizex*900/1000, Sizey*1700/1800, start=-53, extent=-90, style=ARC, outline='black', width=1)

def Update ():
	global xyz, j, u, y, dy, dx, l
	
	xyz=xyz+0.1
	deleteObject(j)
	deleteObject(u)
#вращается мельница	
	brushColor("lightYellow")
	penColor("lightYellow")
	penSize(1)
	j=polygon([(Sizex*(700+(int)(151*sin(xyz)))/1000, Sizey*(250+(int)(151*cos(xyz)))/1800), (Sizex*(700+(int)(151*sin(xyz+0.3)))/1000, Sizey*(250+(int)(151*cos(xyz+0.3)))/1800), (Sizex*(700+(int)(151*sin(xyz+3.141)))/1000, Sizey*(250+(int)(151*cos(xyz+3.141)))/1800), (Sizex*(700+(int)(151*sin(xyz+3.141+0.3)))/1000, Sizey*(250+(int)(151*cos(xyz+3.141+0.3)))/1800)])	
	u=polygon([(Sizex*(700+(int)(151*sin(xyz+1.57)))/1000,
	Sizey*(250+(int)(151*cos(xyz+1.57)))/1800),(Sizex*(700+(int)(151*sin(xyz+0.3+1.57)))/1000,
	Sizey*(250+(int)(151*cos(xyz+0.3+1.57)))/1800),(Sizex*(700+(int)(151*sin(xyz+3.141+1.57)))/1000,
	Sizey*(250+(int)(151*cos(xyz+3.141+1.57)))/1800),(Sizex*(700+(int)(151*sin(xyz+3.141+0.3+1.57)))/1000,
	Sizey*(250+(int)(151*cos(xyz+3.141+0.3+1.57)))/1800)])
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
	l = line(Sizex*900/1000, Sizey*400/1800, Sizex*900/1000, y + Sizey*98/1800 + dy)
	y = y + dy
		
	if y >= Sizey*1000/1800:
		dy = -dy
	if y <= Sizey*380/1800:
		dy = -dy
		 
	
def keyPressed(event):
  if event.keycode == VK_ESCAPE:
    close()  # закрыть окно

     
rot1=c.create_oval(Sizex*0/1000,Sizey*0/1800,Sizex*200/1000, Sizey*200/1800)
rot2=c.create_oval(Sizex*100/1000,Sizey*0/1800,Sizex*300/1000, Sizey*200/1800)
u=c.create_oval(Sizex*0/1000,Sizey*0/1800,Sizex*200/1000, Sizey*200/1800)
j=c.create_oval(Sizex*0/1000,Sizey*0/1800,Sizex*200/1000, Sizey*200/1800)


brushColor('DeepSkyBlue')
rectangle(0, 0, Sizex, Sizey/2)
penColor(0, 0, 0)
penSize(10)
polyline([(Sizex*530/1000, Sizey*1010/1800), (Sizex*700/1000, Sizey*600/1800), (Sizex*900/1000, Sizey*400/1800)])
penSize(1)
c.create_oval (Sizex*650/1000, Sizey*1300/1800, Sizex, Sizey*1550/1800, fill = 'CadetBlue')
c.create_oval (Sizex*700/1000, Sizey*1350/1800, Sizex, Sizey*1500/1800, fill = 'SteelBlue')

x = Sizex*850/1000
dy = -Sizey*5/1800
dx = 0
objp1 = c.create_arc(x, y, x + Sizex*500/1000, y + Sizey*500/1800,start=143, extent=90, style=ARC, outline='black', width=1,fill="blue")
objl2 = c.create_arc(x+Sizex*30/1000, y +Sizey*300/1800,x+Sizex*130/1000, y+Sizey*450/1800, start=245, extent=50, style=ARC, outline='black', width=1)
objh3 = c.create_arc(x-Sizex*353/1000, y+Sizey*32/1800, x+Sizex*127/1000, y+Sizey*532/1800, start=47, extent=-90, style=ARC, outline='black', width=1)

#Fish(x, y)

l = line(Sizex*900/1000, Sizey*400/1800, Sizex*900/1000, Sizey*1000/1800)

Mishka()

Fish2()

Solnce()

polyline([(Sizex*370/1000, Sizey*590/1800), (Sizex*420/1000, Sizey*590/1800), (Sizex*460/1000, Sizey*590/1800), (Sizex*500/1000, Sizey*570/1800)])

penColor(255,0,255)
penSize(5)
brushColor("blue")
rectangle(Sizex*100/1000, Sizey*100/1800, Sizex*300/1000, Sizey*200/1800)
brushColor("yellow")
polygon([(Sizex*100/1000,Sizey*100/1800), (Sizex*200/1000,Sizey*50/1800), (Sizex*300/1000,Sizey*100/1800), (Sizex*100/1000,Sizey*100/1800)])

onKey(keyPressed)
onTimer(Update,50)

run()
