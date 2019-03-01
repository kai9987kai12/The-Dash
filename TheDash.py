import time
import random
import sys
from tkinter import *
from tkinter import ttk
#Questions. MAKESURE THEY'RE DICTIONARY
Q1 = {"question": "Who was the first democratically elected leader of the Russian Federation?", "a": "A:Boris Johnson", "b": "B:Boris Yeltsin", "c": "C: Mikhail Gorbachev"}
Q2 = {"question": "What was the first Carry On film ever made?", "a": "A:Carry On Sergeant", "b": "B:Carry On Cleo", "c": "Carry On Doctor"}
Q3 = {"question": "Why did Tibetans grow long finger nails?", "a": "A:They're attention seekers.", "b": "B:To pick noses efficiently.", "c": "C:To scratch their back."}
Q4 = {"question": "Who signed the Magna Carta", "a": "A:Henry III", "b": "B:King John I", "c": "C:Richard I"}
Q5 = {"question": "What sport was Fanny Chmelar recognized for competing in?", "a": "A:Long Jump", "b": "B:Show Jumping", "c": "C:Ski-ing"}
Q6 = {"question": "Which of these North Korean dictators rules first?", "a": "A:Kim Il-Sung", "b": "B:Kim Jong-Un", "c": "C:Kim Jong-Il"}
Q7 = {"question": "What was Shaun Ryders Auto-biography called?", "a": "A:Twisting My Plums", "b": "B:Twisting My Melon", "c": "C:Twisting My Ankle"}
Q8 = {"question": "Bartommelo Christofori invented what?", "a": "A:The Car", "b": "B:The Piano", "c": "C:The Trumpet"}
Qs = [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8]
Qr = random.choice(Qs)

root = Tk()
Qa = Frame(root)
Qb = Frame(root)
Qc = Frame(root)
QD = Label(root, text=Qr["question"])
DashTable = Frame(root)

#Cash Build Up
CBT = 0

root.resizable(False, False)
root.title("The Dash")
DTEmpty = "******"
DTHOME = "*HOME*"
DTDASHER = "  ↓↓  "

ButtonA = Button(Qa, text=Qr["a"], fg="red")
ButtonB = Button(Qa, text=Qr["b"], fg="red")
ButtonC = Button(Qa, text=Qr["c"], fg="red")

QD.pack()
Qa.pack()
Qb.pack()
Qc.pack()
ButtonA.pack(side=LEFT)
ButtonB.pack(side=LEFT)
ButtonC.pack(side=LEFT)
root.iconbitmap('favicon.ico')  # Set icon
root.mainloop()
