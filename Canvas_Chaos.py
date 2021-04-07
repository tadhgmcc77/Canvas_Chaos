from tkinter import *
import random
import time

def StartGame():
    start1.destroy()
    canvas.delete("all")
    global label1
    label1 = Label(frame ,text = ("Score: %d") % 0, font=("Arial", 44), bg = "black", padx=20,pady=20)
    label1.grid(row=1, column=2)
    global click_time
    click_time = Label(frame, text = "Last Response Time" ,font=("Arial", 16), bg = "white", fg="black", padx=20,pady=20)
    click_time.grid(row=1, column =3)
    global time1
    time1 = time.time()
    drawall()

def drawall():
    if counter1 < 50:
        if counter1 < 40:
            if counter1 < 28:
                if counter1 < 8:
                    drawred()
                elif counter1 < 18:
                    drawred()
                    drawblue()
                else:
                    drawred()
                    drawblue()
                    drawcircle()
                    drawcircle()
            else:
                drawred()
                drawblue()
                drawcircle()
                drawcircle()
                drawgold()
        else:
            drawred()
            drawblue()
            drawcircle()
            drawgold()
            drawblue()
            drawcircle()
    else:
        drawred()
        drawblue()
        drawcircle()
        drawblue()
        drawcircle()
        drawblue()
        drawcircle()
        drawblue()
        drawcircle()
        drawgold()


def drawred():
    canvas.delete("all")
    global time1
    time1 = time.time()
    xpos = random.randint(1,760)
    ypos = random.randint(1,760)
    rect1 = canvas.create_rectangle(xpos, ypos, xpos+40, ypos+40, fill="red")
    canvas.tag_bind(rect1, "<ButtonPress-1>", red)


def drawblue():
    xpos = random.randint(1,760)
    ypos = random.randint(1,760)
    rect2 = canvas.create_rectangle(xpos, ypos, xpos+50, ypos+50, fill="blue")
    canvas.tag_bind(rect2, "<ButtonPress-1>", blue)

def drawcircle():
    xpos = random.randint(1,760)
    ypos = random.randint(1,760)
    circ1 = canvas.create_oval(xpos, ypos, xpos+50, ypos+50, fill="red")
    canvas.tag_bind(circ1, "<ButtonPress-1>", circle)

def drawgold():
    xpos = random.randint(1,760)
    ypos = random.randint(1,760)
    gold1 = canvas.create_oval(xpos, ypos, xpos+20, ypos+20, fill="gold")
    gold2 = canvas.create_line(xpos-10, ypos-10,xpos+30, ypos+30, fill="gold")
    canvas.tag_bind(gold1, "<ButtonPress-1>", gold)
    canvas.tag_bind(gold2, "<ButtonPress-1>", gold)

def red(object):
    x = TimeCheck()
    if x <= 2:
        addtocounter()
    change_label()
    drawall()

def blue(object):
    subfromcounter()
    change_label()
    drawall()

def circle(object):
    global counter1
    counter1 = counter1 - 4
    change_label()
    drawall()

def gold(object):
    x = TimeCheck()
    if x <= 1:
        global counter1
        counter1 = counter1 + 5
    change_label()
    drawall()


def change_label():
    x = TimeCheck()
    global click_time
    click_time.config(text = ("Last Response Time\n %f seconds" % x), font=("Arial", 16), fg="black")
    global counter1
    label1.config(text = ("Score: %d" % counter1), font=("Arial", 44), fg="white")

def TimeCheck():
    global time1
    t = time.time() - time1
    return t


def addtocounter():
    global counter1
    counter1 = counter1 + 1


def subfromcounter():
    global counter1
    counter1 = counter1 - 2

root = Tk()

counter = ()
global counter1
counter1 = 0

global time1
time1 = 0

canvas = Canvas(root, width=800, height=800, bg="black")
canvas.pack(side=TOP)

frame = Frame(root, bg="lightblue", padx = 10, pady = 10)

start1 = Button(frame, text="Start Game!", font=("Arial", 24), command=StartGame, padx = 50, pady = 50, bg="green", fg="white", relief="solid")
start1.grid(row=1, column=2)

tips = "*How To Play*\n Click Red Square within 2s = +1 Point\n Click Blue Square = -2 Points \n Click Red Circle = -4 Points\n Click Golden Snitch within 1s = +5 Points"
tips_label = Label(frame ,text = ("%s" % tips), font=("Arial", 16), bg = "gray", fg="black", pady= 30, padx=10, relief="solid")
tips_label.grid(row=1, column=1)



frame.pack(side=BOTTOM)

root.mainloop()
