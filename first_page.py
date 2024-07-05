from tkinter import *
from tkinter import ttk
import os
import scraping

win = Tk()
win.configure(bg='#99CCFF')
win.state('zoomed')
win.title("Social Listening")

# Initialize style
s = ttk.Style()
s.configure('new.TFrame', background='#99CCFF')

frame = ttk.Frame(win, width=400, height=300, padding=2, style='new.TFrame')

bgimg = PhotoImage(file="social.png")
bg = Label(frame, image=bgimg, bd=1, width=1850, height=320, bg="#FFFFFF")
bg.pack()

ttk.Label(frame, text="Veuillez choisir une marque :", background='#99CCFF', foreground="White", font='Calibri 30').pack(pady=5)
value = StringVar()
Button(frame, width=10, text="Shein", bg='#99CCFF', font='Calibri 30', fg="#000033", activebackground="#b4d0ed", command=lambda: action("Shein")).pack(pady=5)
Button(frame, text="Bershka", width=10, bg='#99CCFF', font='Calibri 30', fg="#000033", activebackground="#b4d0ed", command=lambda: action("Bershka")).pack(pady=5)
Button(frame, text="Pimkie", width=10, bg='#99CCFF', font='Calibri 30', fg="#000033", activebackground="#b4d0ed", command=lambda: action("Pimkie")).pack(pady=5)

marque = ""


def action(val):
    win.destroy()
    global marque
    marque = format(val)
    newwin = Tk()
    newwin.title("Collection de données")
    newwin.state('zoomed')
    newwin.configure(bg="#99CCFF")
    s2 = ttk.Style()
    s2.configure('new.TFrame', background='#99CCFF')
    frame2 = ttk.Frame(newwin, width=400, height=300, padding=2, style='new.TFrame')
    ttk.Label(frame2, text="Marque choisie : " + marque, font='Calibri 35', background="#99CCFF", foreground="#000033").pack(pady=8)
    ttk.Label(frame2, text="Entrain de collecter les données...", font='Calibri 35', background="#99CCFF", foreground="#000033").pack(pady=8)
    ttk.Label(frame2, text="Veuillez patienter", font='Calibri 35', background="#99CCFF", foreground="#000033").pack(pady=8)
    bgimg2 = PhotoImage(file="social.png")
    bg2 = Label(newwin, image=bgimg2, bd=1, width=1850, height=350, bg="#FFFFFF")
    bg2.pack()
    frame2.pack()

    scraping.scraping(marque)

    newwin.after(3000, newwin.destroy)
    newwin.mainloop()
    os.system("python analyse.py")


frame.pack()
win.mainloop()
