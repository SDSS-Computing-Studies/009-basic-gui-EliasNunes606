import tkinter as tk 
from tkinter import *

window = tk.Tk()
window.geometry("260x130")
dogphoto = PhotoImage(file="dog.png")
l1 = tk.Label(window, image=dogphoto)
l2 = tk.Label(window,text="Pochacco!")
l3 = tk.Label(window, text="A cuddly little puppy! This is from the same \n creators who brought you Keropi and Kero Kero", borderwidth=1, bg="#A3FFFF")
l1.place(x=60,y=0)
l2.place(x=127,y=40)
l3.place(x=0,y=95)


window.mainloop()