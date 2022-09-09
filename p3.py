from tkinter import *
import random

window = Tk()
window.geometry('500x200')
laman = Canvas(window, width = 1000, height = 700, bg = "white")
laman.pack()

def game():
    window1 = Toplevel(window)
    window.withdraw()
    window1.geometry('1000x780')
    canvas = Canvas(window1, width = 1000, height = 700, bg = "white")
    canvas.pack()

    timer = Label(window1, text = "60", font = ("Times New Roman", 20))
    timer.place(relx = 0.15, rely = 0.96, anchor = 'sw')

    line = canvas.create_line(0, 0, 0, 0, fill = "grey") # bullet trail
    shooter = canvas.create_rectangle(450, 700, 550, 600, fill = "yellow")
    
    target = canvas.create_oval(475, 250, 525, 300)

    global x
    x = 0
    global a
    a = 0 
    global b
    b = 0

    score = Label(window1, text = 'Score:', font = ("Times New Roman", 20))
    score.pack()
    label = Label(window1, text ='')
    label.pack()

    def countdown(count):  
        timer['text'] = count

        if count > 0:
            window1.after(1000, countdown, count-1)

        elif count == 0:
            win = Toplevel()
            win.geometry('300x150')
            win.wm_title("Score")

            Label(win, text = "Your Score", font = 25).pack()
            Label(win, text = "").pack()
            Label(win, text = point, font = 25).pack()
            Label(win, text = "").pack()
            Button(win, text = "Exit", command = window.destroy).pack()

    def move():
        y = random.randint(-100, 150)
        z = random.randint(-150, 150)

        global a # a = 0
        global x

        window1.after(600, move)
        a = a + 1 # a = 0

        if a % 3 == 0: # a = 0
            canvas.coords(target, 475, 250, 525, 300)
        canvas.move(target, y, z)

    def red():
        canvas.itemconfig(target, fill = "red")

    def green():
        canvas.itemconfig(target, fill = "green")

    def blue():
        canvas.itemconfig(target, fill = "blue")
        
    def mouse(event):
        global x # x = 0
        global b # b = 0
        global point

        canvas.coords(line, 500, 700, event.x, event.y)
        coord0 = canvas.coords(line)[0]
        coord1 = canvas.coords(line)[1]
        coord2 = canvas.coords(line)[2]
        coord3 = canvas.coords(line)[3]

        if canvas.find_overlapping(coord0, coord1, coord2 ,coord3) != (1,2,3,4):
            x = x + 10 # score
            point = x
            label.configure(text = x, font = ("none", 20))

        if b == 0:
            move()
            countdown(60)
        b = b + 1  # b = 0

    lab = Label(window1, text = "Choose Color :")
    lab.place(relx = 0.82, rely = 0.905, anchor = "nw")

    ez = Button(window1, text = "Red", command = red)
    ez.place(relx = 0.80, rely = 0.94, anchor = "nw")

    med = Button(window1, text = "Green", command = green)
    med.place(relx = 0.845, rely = 0.94, anchor = "nw")

    sus = Button(window1, text = "Blue", command = blue)
    sus.place(relx = 0.90, rely = 0.94, anchor = "nw")

    canvas.tag_bind(target, "<Button-1>", mouse)

lbldif = Label(laman, text = "AimLab Wannabe", font = ("Times New Roman", 25), bg = "white")
lbldif.place(x = 250,y = 30, anchor = 'center')

lbl2 = Label(laman, text = "Aim  Practice", font = ("Times New Roman", 13), bg = "white")
lbl2.place(x = 250, y = 62, anchor = 'center')

playbtn = Button(laman,text = "Play", height = 2,width = 10,command = game)
playbtn.place(x = 150,y = 120)

exitbtn = Button(laman,text = "Exit", height = 2,width = 10,command = window.destroy)
exitbtn.place(x = 275,y = 120)

window.mainloop()