import sys #to import system files
import cv2
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import time



localtime = time.localtime(time.time())

root = Tk()
root.title('Tampilan')
root.geometry('1366x768')
bg=ImageTk.PhotoImage(Image.open("output.jpg"))

#command=lambda: retrieve_input() >>> just means do this when i press the button
#buttonCommit.pack()

def DClock():
    curr_time= time.strftime("%H:%M:%S")
    curr_date= time.strftime("%A %d/%b/%Y")
    clock.config(text=curr_time)
    date.config(text=curr_date)
    clock.after(100,DClock)

# Show image using label 
Label(root, image = bg).place(x = 0, y = 0) 

clock= Label(root, font=("times",20,"bold"),fg="black")
clock.grid(row=1,column=0, padx=10, pady=10)
date= Label(root, font=("times",20,"bold"),fg="black")
date.grid(row=2,column=0, padx=10, pady=10)
DClock()

Label(root, text="Pengunjung Masuk : 8", font=("Helvetica",15), fg="black").place(x=10, y=120)
Label(root, text="Pengunjung di dalam : 10", font=("Helvetica",15), fg="black").place(x=10, y=160)
Label(root, text="Max Pengunjung :", font=("Helvetica",15), fg="red").place(x=10, y=200)
Label(root, text="- MAX PENGUNJUNG MENCAPAI BATAS -", font=("Helvetica",20), fg="red").place(x=750, y=350, anchor="center")

mainloop()