import tkinter as tk
from PIL import ImageTk, Image
import sys

window = tk.Tk()
label = tk.Label(text="Pokemon")
label.pack()

global button1, button2, button3, button4, buttonState, lastState

buttonState="Outside"
frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
frame.pack(side=tk.BOTTOM)
button1 = tk.Button(master=frame, text="Gym 1", height=5, width=15)
button1.pack(side=tk.LEFT)
button2 = tk.Button(master=frame, text="Wild", height=5, width=15)
button2.pack(side=tk.LEFT)
button3 = tk.Button(master=frame, text="Menu", height=5, width=15)
button3.pack(side=tk.LEFT)
button4 = tk.Button(master=frame, text="Quit", height=5, width=15)
button4.pack(side=tk.LEFT)



def activepokemon():
  global activepkm
  frame = tk.Frame(window)
  frame.pack()
  frame.place(anchor='center', relx=0.18, rely=0.62)
  img2=Image.open("25.png")
  img = ImageTk.PhotoImage(img2.resize((100,100), Image.Resampling.LANCZOS))
  activepkm = tk.Label(frame, image = img)
  activepkm.pack()
  buttonListner()

def handle_clickGym(event):
  global button1, button2, button3, button4, buttonState, lastState, activepkm
  buttonState="GymFight" 
  button1["text"]="Fight"
  button2["text"]="Potion"
  button3["text"]="Run"
  button4["text"]=""
  activepokemon()

def handle_clickRun(event):
  global button1, button2, button3, button4, buttonState, activepkm
  activepkm.after(1,activepkm.destroy)
  buttonState="Outside"
  button1["text"]="Gym 1"
  button2["text"]="Wild"
  button3["text"]="Menu"
  button4["text"]="Quit"
  buttonListner()
def handle_clickWild(event):
  global button1, button2, button3, button4, buttonState, lastState
  buttonState="WildFight"
  lastState="WildFight"
  button1["text"]="Fight"
  button2["text"]="Catch"
  button3["text"]="Run"
  button4["text"]=""
  activepokemon()
def handle_clickFight(event):
  global button1, button2, button3, button4, buttonState, lastState
  buttonState="Fight"
  button1["text"]="Attack A"
  button2["text"]="Attack B"
  button3["text"]="Attack C"
  button4["text"]="Attack D"
  buttonListner()

def handle_clickAttackA(event):
  global buttonState, lastState
  print("ATTACK A")##Perform attack A##
  if lastState=="GymFight":
    handle_clickGym("<Button-1>")
  elif lastState=="WildFight":
    handle_clickWild("<Button-1>")

def handle_clickAttackB(event):
  global buttonState, lastState
  print("ATTACK B")##Perform attack B##
  if lastState=="GymFight":
    handle_clickGym("<Button-1>")
  elif lastState=="WildFight":
    handle_clickWild("<Button-1>")

def handle_clickAttackC(event):
  global buttonState, lastState
  print("Attack C")##Perform attack C##
  if lastState=="GymFight":
    handle_clickGym("<Button-1>")
  elif lastState=="WildFight":
    handle_clickWild("<Button-1>")

def handle_clickAttackD(event):
  global buttonState, lastState
  print("ATTACK D")##Perform attack D##
  if lastState=="GymFight":
    handle_clickGym("<Button-1>")
  elif lastState=="WildFight":
    handle_clickWild("<Button-1>")
    
def handle_clickPotion(event):
  global buttonState, lastState
  print("Used Potion")##Performs Potion##
  if lastState=="GymFight":
    handle_clickGym("<Button-1>")
  elif lastState=="WildFight":
    handle_clickWild("<Button-1>")

def handle_clickCatch(event):
  global buttonState, lastState
  print("Attempting Catch")##Performs Catch##
  if lastState=="GymFight":
    handle_clickGym("<Button-1>")
  elif lastState=="WildFight":
    handle_clickWild("<Button-1>")


def handle_clickQuit(event):
  print("Quitting...")
  sys.exit()
  
def buttonListner():                                              
  if buttonState=="Outside":                          ##Sets state as Outside
    print(buttonState)                                ##Button 1 goes to Gym, button 2 goes to Wild
    button1.bind("<Button-1>", handle_clickGym)                     
    button2.bind("<Button-1>", handle_clickWild)
    button4.bind("<Button-1>", handle_clickQuit)
  if buttonState=="GymFight":                         ##Sets state as Gym
    print(buttonState)                                ##Button 1 goes to Fight, button 2 goes to
    button1.bind("<Button-1>", handle_clickFight)     ##Potion, button 3 goes to Outside
    button2.bind("<Button-1>", handle_clickPotion)
    button3.bind("<Button-1>", handle_clickRun)
    button4.unbind("<Button-1>")
  if buttonState=="WildFight":                        ##Sets state as Wild
    print(buttonState)                                ##Button 1 goes to Fight, button 2 goes to
    button1.bind("<Button-1>", handle_clickFight)     ##Outside
    button2.bind("<Button-1>", handle_clickCatch)
    button3.bind("<Button-1>", handle_clickRun)
    button4.unbind("<Button-1>")
  if buttonState=="Fight":                            ##Sets state as Fight, Attacks then goes back
    print(buttonState)
    button1.bind("<Button-1>",handle_clickAttackA)
    button2.bind("<Button-1>",handle_clickAttackB)
    button3.bind("<Button-1>",handle_clickAttackC)
    button4.bind("<Button-1>",handle_clickAttackD)
  window.mainloop()
buttonListner()
window.mainloop()

