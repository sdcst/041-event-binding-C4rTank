import tkinter as tk
import playsound as p

def Note_C4(event):
    print(event)
    p.playsound("C4.mp3",block=False)
def Note_D4(event):
    print(event)
    p.playsound("D4.mp3",block=False)
def Note_E4(event):
    print(event)
    p.playsound("E4.mp3",block=False)
def Note_F4(event):
    print(event)
    p.playsound("F4.mp3",block=False)
def Note_G4(event):
    print(event)
    p.playsound("G4.mp3",block=False)
def Note_A4(event):
    print(event)
    p.playsound("A4.mp3",block=False)
def Note_B4(event):
    print(event)
    p.playsound("B4.mp3",block=False)
    
#-----------------------------------------------------------------------------------------

def Note_C5(event):
    print(event)
    p.playsound("C5.mp3",block=False)
def Note_D5(event):
    print(event)
    p.playsound("D5.mp3",block=False)
def Note_E5(event):
    print(event)
    p.playsound("E5.mp3",block=False)
def Note_F5(event):
    print(event)
    p.playsound("F5.mp3",block=False)
def Note_G5(event):
    print(event)
    p.playsound("G5.mp3",block=False)
def Note_A5(event):
    print(event)
    p.playsound("A5.mp3",block=False)
def Note_B5(event):
    print(event)
    p.playsound("B5.mp3",block=False)

def Note_C6(event):
    print(event)
    p.playsound("C6.mp3",block=False)

#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------

win = tk.Tk()
win.attributes('-topmost',True)
win.title("Soundboard/Paino")
win.geometry("825x150")

#-------------------------------------------------------------------------------------

c4 = tk.Button(win,text="C4",borderwidth=5,command="playsound")
c4.place(x=0,y=0,width=55,height=150)
c4.bind("<Button>",Note_C4)

d4 = tk.Button(win,text="D4",borderwidth=5,command="playsound")
d4.place(x=55,y=0,width=55,height=150)
d4.bind("<Button>",Note_D4)

e4 = tk.Button(win,text="E4",borderwidth=5,command="playsound")
e4.place(x=110,y=0,width=55,height=150)
e4.bind("<Button>",Note_E4)

f4 = tk.Button(win,text="F4",borderwidth=5,command="playsound")
f4.place(x=165,y=0,width=55,height=150)
f4.bind("<Button>",Note_F4)

g4 = tk.Button(win,text="G4",borderwidth=5,command="playsound")
g4.place(x=220,y=0,width=55,height=150)
g4.bind("<Button>",Note_G4)

a4 = tk.Button(win,text="A4",borderwidth=5,command="playsound")
a4.place(x=275,y=0,width=55,height=150)
a4.bind("<Button>",Note_A4)

b4 = tk.Button(win,text="B4",borderwidth=5,command="playsound")
b4.place(x=330,y=0,width=55,height=150)
b4.bind("<Button>",Note_B4)

#-------------------------------------------------------------------------------------

c5 = tk.Button(win,text="C5",borderwidth=5,command="playsound")
c5.place(x=385,y=0,width=55,height=150)
c5.bind("<Button>",Note_C5)

d5 = tk.Button(win,text="D5",borderwidth=5,command="playsound")
d5.place(x=440,y=0,width=55,height=150)
d5.bind("<Button>",Note_D5)

e5 = tk.Button(win,text="E5",borderwidth=5,command="playsound")
e5.place(x=495,y=0,width=55,height=150)
e5.bind("<Button>",Note_E5)

f5 = tk.Button(win,text="F5",borderwidth=5,command="playsound")
f5.place(x=550,y=0,width=55,height=150)
f5.bind("<Button>",Note_F5)

g5 = tk.Button(win,text="G5",borderwidth=5,command="playsound")
g5.place(x=605,y=0,width=55,height=150)
g5.bind("<Button>",Note_G5)

a5 = tk.Button(win,text="A5",borderwidth=5,command="playsound")
a5.place(x=660,y=0,width=55,height=150)
a5.bind("<Button>",Note_A5)

b5 = tk.Button(win,text="B5",borderwidth=5,command="playsound")
b5.place(x=715,y=0,width=55,height=150)
b5.bind("<Button>",Note_B5)

c6 = tk.Button(win,text="C6",borderwidth=5,command="playsound")
c6.place(x=770,y=0,width=55,height=150)
c6.bind("<Button>",Note_C6)

win.mainloop()

#done