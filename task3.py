import tkinter as tk 
from tkinter import *

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")

dogphoto = PhotoImage(file="dog.png")
label = tk.Label(window, image=dogphoto)
label1 = tk.Label(window,text="Pochacco")
label2 = tk.Label(window,text="A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero",background='#A3FFFF')
label.grid(row = 1, column = 1,sticky=E)
label1.grid(row = 1, column = 2,sticky=W)
label2.grid(row = 2,column = 1, columnspan = 2)





window.mainloop()