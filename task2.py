import tkinter as tk 
from tkinter import *

window = tk.Tk()
window.geometry("600x200")
window.title("T-Town Veterinary Clinic Database")

dogphoto = PhotoImage(file="dog.png")
label = tk.Label(window, image=dogphoto)
label.grid(row=1,column=1)

label1 = tk.Label(window,text="Client Database")
label1.grid(row=1,column=3)













window.mainloop()