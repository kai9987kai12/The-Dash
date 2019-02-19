import time
import random
import sys
from tkinter import *
from tkinter import ttk

#Questions. MAKESURE THEY'RE DICTIONARY
window = Tk()
 
window.title("Random question generator V1.0")
Q1 = {"question": "Who was the first democratically elected leader of the Russian Federation?", "a": "A:Boris Johnson", "b": "B:Boris Yeltsin", "c": "C: Mikhail Gorbachev"}
Q2 = {"question": "What was the first Carry On film ever made?", "a": "A:Carry On Sergeant", "b": "B:Carry On Cleo", "c": "Carry On Doctor"}
Q3 = {"question": "Why did Tibetans grow long finger nails?", "a": "A:They're attention seekers.", "b": "B:To pick noses efficiently.", "c": "To scratch their back."}
Q4 = {"question": "Who signed the Magna Carta", "a": "A:Henry III", "b": "B:King John I", "c": "Richard I"}
Q5 = {"question": "What sport was Fanny Chmelar recognized for competing in?", "a": "A:Long Jump", "b": "B:Show Jumping", "c": "Ski-ing"}
Q6 = {"question": "What sport was Fanny Chmelar recognized for competing in?", "a": "A:Long Jump", "b": "B:Show Jumping", "c": "Ski-ing"}
Q7 = {"question": "Which of these North Korean dictators rules first?", "a": "A:Kim Il-Sung", "b": "B:Kim Jong-Un", "c": "Kim Jong-Il"}
Q8 = {"question": "What was Shaun Ryders Auto-biography called?", "a": "A:Twisting My Plums", "b": "B:Twisting My Melon", "c": "Ski-ing"}
Q9 = {"question": "What car did elon musk sent into space?", "a": "Audi", "b": "Honda", "c": "Tesla"}
Q10 = {"question": "What is the UK?""A:City", "b": "Country", "c": "B:State"}
Q11 = {"question": "Who is better?""A:PewDiePie", "b": "T-Series", "c": "B:I hate them both"}
Random= [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10 , Q11]
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

