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
import time

def Fish (x, y):
    c.create_arc(x, y, x + 500, y + 500,start=143, extent=90, style=ARC, outline='black', width=1)
    c.create_arc(x+30, y +300,x +130, y + 450, start=245, extent=50, style=ARC, outline='black', width=1)
    c.create_arc(x-353, y + 32, x + 127, y +532, start=47, extent=-90, style=ARC, outline='black', width=1)
    
def Update ():
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

	
c = canvas()
c.pack()
canvasSize(1000, 1800)
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
objp1 = c.create_arc(x, y, x + 500, y + 500,start=143, extent=90, style=ARC, outline='black', width=1)
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
rectangle(680, 100, 720, 400)
rectangle(550, 230, 850, 270)
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
