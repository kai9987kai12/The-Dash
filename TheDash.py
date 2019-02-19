import time
import random
import sys
from tkinter import *
from tkinter import ttk

#Questions. MAKESURE THEY'RE DICTIONARY
window = Tk()
 
window.title("Random question generator V1.0")
Q1 = "Question: Who was the first democratically elected leader of the Russian Federation?, A: Boris Johnson, B: Boris Yeltsin, C: Mikhail Gorbachev"
Q2 = "Question: What was the first Carry On film ever made?, A: Carry On Sergeant, B: Carry On Cleo, C: Carry On Doctor"
Q3 = "Question: Why did Tibetans grow long finger nails?, A: They're attention seekers., B: To pick noses efficiently., C: To scratch their back."
Q4 = "Question: Who signed the Magna Carta, A:Henry III, B: B:King John I, C: Richard I"
Q5 = "Question: What sport was Fanny Chmelar recognized for competing in?, A: Long Jump, B: Show Jumping, C: Ski-ing"
Q6 = "Question: Which of these North Korean dictators rules first?, A: Kim Il-Sung, B: Kim Jong-Un, C: Kim Jong-Il"
Q7 = "Question: What was Shaun Ryders Auto-biography called?, A: Twisting My Plums, B: Twisting My Melon, C: Ski-ing"
Q8 = "Question: What car did elon musk sent into space?, A: Audi, B: Honda, C: Tesla"
Q9 = "Question: What is the UK? A: City, B: Country, C: B:State"
Q10 = "Question: Who is better? A:PewDiePie, b: T-Series, c: B:I hate them both"
Random= [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10]
def new():
    lbl.configure(text= random.choice(Random))
def Close():
    window.destroy()
lbl = Label(window, text=random.choice(Random))
lbl.grid(column=0, row=0)
ttk.Button(window, text="New Question", command=new).grid(row=2, column=0)
ttk.Button(window, text="Close", command=Close).grid(row=3, column=0)
window.resizable(False, False)
window.iconbitmap('favicon.ico')
window.attributes("-topmost", True)
window.mainloop()
