
import turtle
import random
from math import*
import tkinter as tk

colorlist = ["red", "green", "blue", "orange", "magenta", "lime", "purple", "gray", "black", "yellow"]
n = 3

stop = False

#n = int(screen.textinput("Number of points", "How many points do you want?"))
#=============================================================================================================

def stop():
    global stop
    stop = True

def Add_points():
    global n
    n += 1
    print("n = " + str(n))

def remove_points():
    global n
    n -= 1
    print("n = " + str(n))

def start():
    global stop
    stop = False
    canvas.delete("all")
    fractal(n)


def fractal(n):

    d = (n-1)

    cursor = turtle.RawTurtle(canvas)
    cursor.shape("circle")
    cursor.penup()
    cursor.color("yellow")
    cursor.pensize(1)
    cursor.speed(0)

    x = random.randint(-250,250)
    y = random.randint(-250,250)

    cursor.setposition(x, y)
    cursor.dot(6, "cyan")

    for a in range (n):
        cursor.setposition(round(200*cos((2*pi/n)*a)),round(200*sin((2*pi/n)*a)))
        cursor.dot(6,"black")
    
    for a in range(10000):
        r = random.randint(0,n)
        if stop == True:
            break
        for v in range(0, n):
            if v == r:
                cursor.setposition(round((x+200*cos((2*pi/n)*v))/d),round((y+200*sin((2*pi/n)*v))/d))
                cursor.dot(3, colorlist[v%10])
                x = round((x+200*cos((2*pi/n)*v))/d)
                y = round((y+200*sin((2*pi/n)*v))/d)
#=============================================================================================================

root = tk.Tk()
canvas = tk.Canvas(master = root, width = 500, height = 500)
canvas.pack()


cursor = turtle.RawTurtle(canvas)
cursor.shape("circle")
cursor.penup()
cursor.color("yellow")
cursor.pensize(1)
cursor.speed(0)



tk.Button(master = root, text = "start", command = start).pack(side = tk.LEFT)

tk.Button(master = root, text = "add points", command = Add_points).pack(side = tk.LEFT)

tk.Button(master = root, text = "remove points", command = remove_points).pack(side = tk.LEFT)

tk.Button(master = root, text = "stop", command = stop).pack(side = tk.LEFT)



root.mainloop()

#=============================================================================================================


