import tkinter as tk
import random
import time
w = tk.Tk()
w.geometry("600x400")
w.title("map")
img = tk.PhotoImage(file="Images/guy.png")
c = tk.Canvas(width=550,height=450,background="#9689dd",bd="2")
c.pack()
c.create_image(300,200, image=img)
areaTopLeft = [ (0,0), (random.randint(0, 600), random.randint(0, 400)), (random.randint(0, 600), random.randint(0, 400)), (random.randint(0, 600), random.randint(0, 400)), (random.randint(0, 600), random.randint(0, 400)), (random.randint(0, 600), random.randint(0, 400)), (random.randint(0, 600), random.randint(0, 400)), (random.randint(0, 600), random.randint(0, 400)), (random.randint(0, 600), random.randint(0, 400))]
speed = 1

collectables = [(random.randint(0, 600), random.randint(0, 400)), (random.randint(0, 600), random.randint(0, 400)), (random.randint(0, 600), random.randint(0, 400))]
score = 0
posList = []
for i in areaTopLeft:
    x = c.create_rectangle(i,i[0] + 10, i[1] + 10,fill="#aa0000")
    posList.append(x)

colList = []
for i in collectables:
    x = c.create_rectangle(i,i[0] + 5, i[1] + 5,fill="Purple")
    colList.append(x)

def collectableCol():
    global score, speed, colTime
    
    pos = c.coords(rec)
    for i in colList:
        if i in c.find_overlapping(pos[0], pos[1], pos[2], pos[3]):
            score += 1
            speed += 0.1
            colTime = time.time()
            print(score)
            c.itemconfigure(text, text=f"{score}, Speed = {round(speed, 3)}")
            c.delete(i)
            colList.pop(colList.index(i))
    print(colList)
    if not colList:
        collectables = [(random.randint(0, 550), random.randint(0, 350)), (random.randint(0, 550), random.randint(0, 350)), (random.randint(0, 550), random.randint(0, 350))]
        for i in collectables:
            x = c.create_rectangle(i,i[0] + 5, i[1] + 5,fill="Purple")
            colList.append(x)


def collision(x = 0, y = 0):
    pos = c.coords(rec)
    for i in posList:
        if i in c.find_overlapping(pos[0]+x, pos[1]+y, pos[2]+x, pos[3]+y):
            return True
    return False


text = c.create_text(100, 30, text = f"{score}\nPress ESC to\nreset collectables", font = "monaco")
rec = c.create_rectangle(50,50,80,80,fill="Black")
def keyPress(e):
        global cur
        cur = time.time()
        collectableCol()
        if e.keysym == "Left":
            if collision(-5, 0):
                pass
            else:
                c.move(rec,-5 * speed,0 * speed) 

        if e.keysym == "Right":
            if collision(5, 0):
                pass
            else:
                c.move(rec,5 * speed,0 * speed)
            #c.move(rec,5,0)    
        if e.keysym == "Up":
            if collision(0, -5):
                pass
            else:
                c.move(rec,0 * speed,-5 * speed)
            #c.move(rec,0,-5) 
        if e.keysym == "Down":
            if collision(0, 5):
                pass
            else:
                c.move(rec,0 * speed,5 * speed)
            #c.move(rec,0,5) 
        if e.keysym == "Escape":
            for i in colList:
                c.delete(i)
                colList.pop(colList.index(i))
            collectables = [(random.randint(0, 550), random.randint(0, 350)), (random.randint(0, 550), random.randint(0, 350)), (random.randint(0, 550), random.randint(0, 350))]
            for i in collectables:
             x = c.create_rectangle(i,i[0] + 5, i[1] + 5,fill="Purple")
             colList.append(x)
        #speedDown()


def speedDown():
    global cur, colTime, speed
    #if (cur - 5) > colTime:
    speed -= 0.01
    if speed < 0:
        speed = 0
    print("speedDown")
    c.itemconfigure(text, text=f"{score}, Speed = {round(speed, 3)}")
    w.after(1000,speedDown)
    cur = time.time()
    colTime = time.time()

def go(e):
    speedDown()

w.bind("<Left>",keyPress)
w.bind("<Right>",keyPress)#
w.bind("<Up>",keyPress)
w.bind("<Down>",keyPress)
w.bind("<Escape>", keyPress)
w.after(1000,speedDown)


w.mainloop()