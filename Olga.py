from tkinter import*
from graph import*

c=canvas()
Sizex=500
Sizey=500
windowSize(Sizex, Sizey)
canvasSize(Sizex, Sizey)

penColor(0,0,50 )
brushColor(0,0,50)
rectangle(0,0,Sizex*400/400,Sizex*400/400)

def update():
    moveObjectBy(obj1, -3*Sizex/400, 0)
    moveObjectBy(obj2, -3*Sizex/400, 0)
    moveObjectBy(obj3, -3*Sizex/400, 0)
    moveObjectBy(obj4, -3*Sizex/400, 0)
    moveObjectBy(obj5, -3*Sizex/400, 0)
    moveObjectBy(obj6, -3*Sizex/400, 0)
    moveObjectBy(obj7, -3*Sizex/400, 0)
    moveObjectBy(obj8, -3*Sizex/400, 0)
    moveObjectBy(obj9, -3*Sizex/400, 0)
    if yCoord(obj9) ==0:
        close()
def keyPressed(event):
    if event.keycode == VK_ESCAPE:
        close()
onKey(keyPressed)
x = Sizex*400/400
y = Sizey*170/400
penColor(100,100,100)
brushColor(100,100,100)
obj1=c.create_oval(x - 50*Sizex/400, y-70*Sizey/400, x + Sizex*50/400, y + 30*Sizey/400, fill = "grey", outline = "grey")
obj2=c.create_oval(x - 95*Sizex/400, y-35*Sizey/400, x-Sizex*25/400, y + 35*Sizey/400, fill = "grey", outline = "grey")
obj3=c.create_oval(x+30*Sizex/400, y-30*Sizey/400, x + Sizex*90/400, y + 30*Sizey/400, fill = "grey", outline = "grey")
obj4=c.create_oval(x+150*Sizex/400, y+130*Sizey/400, x + Sizex*250/400, y + 230*Sizey/400, fill = "grey", outline = "grey")
obj5=c.create_oval(x+105*Sizex/400, y+165*Sizey/400, x + Sizex*175/400, y+235*Sizey/400, fill = "grey", outline = "grey")
obj6=c.create_oval(x+230*Sizex/400, y+170*Sizey/400, x + Sizex*290/400, y+230*Sizey/400, fill = "grey", outline = "grey")
obj7=c.create_oval(x+350*Sizex/400, y-70*Sizey/400, x + Sizex*450/400, y+30*Sizey/400, fill = "grey", outline = "grey")
obj8=c.create_oval(x+305*Sizex/400, y-35*Sizey/400, x + Sizex*375/400, y+35*Sizey/400, fill = "grey", outline = "grey")
obj9=c.create_oval(x+430*Sizex/400, y-30*Sizey/400, x + Sizex*490/400, y+30*Sizey/400, fill = "grey", outline = "grey")

onKey(keyPressed)
onTimer(update, 50)



penColor(250, 150, 50)
brushColor(220, 100, 0)
polygon([(Sizex*267/500, Sizey*120/500), (Sizex*240/500, Sizey*100/500), (Sizex*210/500, Sizey*85/500), (Sizex*250/500, Sizey*95/500), (Sizey*270/500, Sizey*110/500)])
polygon([(Sizex*230/500, Sizey*180/500), (Sizex*225/500, Sizey*195/500), (Sizex*230/500, Sizey*210/500), (Sizex*225/500, Sizey*210/500), (Sizex*222/500, Sizey*208/500), (Sizex*225/500, Sizey*215/500), (Sizex*235/500, Sizey*215/500), (Sizex*240/500, Sizey*200/500), (Sizex*248/500, Sizey*195/500)])
polygon([(Sizex*180/500, Sizey*170/500), (Sizex*175/500, Sizey*185/500), (Sizex*180/500, Sizey*200/500), (Sizex*175/500, Sizey*200/500), (Sizex*172/500, Sizey*198/500), (Sizex*175/500, Sizey*205/500), (Sizex*185/500, Sizey*205/500), (Sizex*190/500, Sizey*190/500), (Sizex*198/500,Sizey*185/500), (Sizex*210/500, Sizey*170/500)])
polygon([(Sizex*230/500, Sizey*150/250), (Sizex*220/500, Sizey*140/500), (Sizex*220/500, Sizey*130/500), (Sizex*230/500, Sizey*120/500), (Sizex*210/500, Sizey*100/500), (Sizex*200/500, Sizey*100/500), (Sizex*180/500, Sizey*100/500), (Sizex*140/500, Sizey*115/500), (Sizex*120/500, Sizey*123/500), (Sizex*100/500, Sizey*130/500), (Sizex*95/500, Sizey*145/500), (Sizex*105/500, Sizey*135/500), (Sizex*107/500, Sizey*132/500), (Sizex*190/500, Sizey*120/500), (Sizex*210/500, Sizey*135/500), (Sizex*210/500, Sizey*140/500), (Sizex*220/500, Sizey*150/500), (Sizex*230/500, Sizey*150/500)])

brushColor(255, 150, 0)
polygon([(Sizex*257/500, Sizey*125/500), (Sizex*230/500, Sizey*105/500), (Sizex*200/500, Sizey*90/500), (Sizex*240/500, Sizey*100/500), (Sizex*260/500, Sizey*115/500), (Sizex*257/500, Sizey*125/500)])
polygon([(Sizex*50/500, Sizey*180/500), (Sizex*90/500, Sizey*190/500), (Sizex*115/500, Sizey*178/500), (Sizex*125/500, Sizey*165/500), (Sizex*145/500, Sizey*150/500), (Sizex*160/500, Sizey*145/500), (Sizex*200/500, Sizey*150/500), (Sizex*210/500, Sizey*150/500), (Sizex*230/500, Sizey*150/500), (Sizex*250/500, Sizey*140/500), (Sizex*255/500, Sizey*130/500), (Sizex*260/500, Sizey*115/500), (Sizex*270/500, Sizey*110/500), (Sizex*288/500, Sizey*120/500), (Sizex*290/500, Sizey*127/500), (Sizex*310/500, Sizey*140/500), (Sizex*310/500, Sizey*145/500), (Sizex*307/500, Sizey*154/500), (Sizex*305/500, Sizey*150/500),(Sizex*285/500, Sizey*150/500), (Sizex*285/500, Sizey*145/500), (Sizex*275/500, Sizey*148/500), (Sizex*265/500, Sizey*160/500), (Sizex*265/500, Sizey*170/500), (Sizex*255/500, Sizey*180/500), (Sizex*250/500, Sizey*190/500), (Sizex*240/500, Sizey*200/500), (Sizex*220/500, Sizey*200/500), (Sizex*190/500, Sizey*185/500), (Sizex*165/500, Sizey*190/500), (Sizex*150/500, Sizey*180/500), (Sizex*130/500, Sizey*195/500), (Sizex*100/500, Sizey*205/500), (Sizex*80/500, Sizey*200/500)])
polygon([(210, 150), (200, 140), (200, 130), (210, 120), (190, 100), (180, 100), (160, 100), (120, 115), (100, 123), (80, 130), (75, 145), (85, 135), (87, 132), (170, 120), (190, 135), (190, 140), (200, 150), (210, 150)])
polygon([(210, 180), (205, 195), (210, 210), (205, 210), (202, 208), (205, 215), (215, 215), (220, 200), (228, 195), (240, 180)])
polygon([(160, 170), (155, 185), (160, 200), (155, 200), (152, 198), (155, 205), (165, 205), (170, 190), (178,185), (190, 170)])
polygon([(40, 175), (70, 170), (55, 181), (60, 200)])

penColor(0, 0, 0)
penSize(2)
moveTo(280, 129)
lineTo(275, 127)
lineTo(280, 127)
penColor(0, 100, 255)
penSize(5)
point(280, 128)



run()
