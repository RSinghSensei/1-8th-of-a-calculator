#I can construct a calculator lol
#Tkinter GUI
#Now it's just a matter of layout and adding new functions

from tkinter import *

new_Win= Tk()
new_Win.geometry('400x600')
display =""
disp_Label = StringVar()

def PressF(num):
    global display
    display = display + str(num)
    disp_Label.set(display)
def equals():
    total = eval(display)
    disp_Label.set(total)

button1 = Button(new_Win,
                 text="5",
                 command=lambda : PressF(5))
button2 = Button(new_Win,
                text="1",
                command=lambda : PressF(1))
button3 = Button(new_Win,
                text="2",
                command=lambda: PressF(2))
button4 = Button(new_Win,
                text="3",
                command=lambda: PressF(3))
button5 = Button(new_Win,
                 text="+",
                 command= lambda: PressF('+'))
button6 = Button(new_Win,
                 text = "=",
                 command = equals)
button6.pack()
label = Label(new_Win,
              textvariable = disp_Label,
              font = ('consolas',20),
              bg = "white",
              width = 24,
              )
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()

label.pack()

new_Win.mainloop()


