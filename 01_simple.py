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

c = canvas()
c.pack()
canvasSize(1000, 1800)
brushColor('DeepSkyBlue')
rectangle(0, 0, 1000, 900)
penColor(0, 0, 0)
penSize(10)
polyline([(530, 1010), (700, 600), (900, 400)])
penSize(1)
c.create_oval (650, 1300, 1000, 1550, fill = 'CadetBlue')
c.create_oval (700, 1350, 1000, 1500, fill = 'SteelBlue')
line(900, 400, 900, 1400)
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
polygon([(100,100), (200,50), 
         (300,100), (100,100)])
run()
