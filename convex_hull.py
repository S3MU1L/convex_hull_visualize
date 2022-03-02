import tkinter
import random
root = tkinter.Tk()
WIDTH = 700
HEIGHT = 700
points = []
def click(event):
    global points
    x = event.x
    y = event.y
    points.append((x,y))
    r = 10
    canvas.create_oval(x-r,y-r,x+r,y+r,fill = "black")

def ccw(a,b,c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])

def gen():
    global points
    r = 10
    points += [(random.randint(r,WIDTH-r),(random.randint(r,HEIGHT-r))) for i in range(40)]
    dots()

def dots():
    for point in points:
        x = point[0]
        y = point[1]
        r = 10
        canvas.create_oval(x - r, y - r, x + r, y + r, fill="black")

def res():
    global points
    canvas.delete("all")
    points = []


def kresli():
    canvas.delete("all")
    global u_hull,d_hull,hull
    points.sort()
    u_hull = []
    d_hull = []
    hull = []
    #we must draw all the points firstly
    dots()
    for point in points:
        while len(u_hull)>=2 and ccw(u_hull[-2],u_hull[-1],point) <= 0:
            u_hull.pop()
        u_hull.append(point)

    for point in reversed(points):
        while len(d_hull)>=2 and ccw(d_hull[-2],d_hull[-1],point) <= 0:
            d_hull.pop()
        d_hull.append(point)

    hull = d_hull+u_hull
    for point in hull:
        r = 10
        canvas.create_oval(point[0]-r,point[1]-r,point[0]+r,point[1]+r,fill = "green")


    for i in range(len(hull)-1):
        x0,y0,x1,y1 = hull[i][0],hull[i][1],hull[i+1][0],hull[i+1][1]
        canvas.create_line(x0,y0,x1,y1,fill = "red")



canvas = tkinter.Canvas(root,width = WIDTH,height = HEIGHT,bg = "white")
canvas.grid(row = 0, column = 0,columnspan = 3)
draw = tkinter.Button(root,text = "DRAW", fg = "#0000FF", width = 20, height = 5, command = kresli, bg = "#9FD26F")
draw.grid(row = 1, column = 0)
restart = tkinter.Button(root,text = "RESTART", fg = "#0000FF", width = 20, height = 5, command = res, bg = "#9FD26F")
restart.grid(row = 1, column = 1)
generate = tkinter.Button(root, text = "GENERATE", fg = "#0000FF", width = 20, height = 5, command = gen , bg = "#9FD26F")
generate.grid(row = 1, column = 2)
canvas.bind('<Button-1>',click)
root.mainloop()