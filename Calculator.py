from tkinter import *
# this function transfers inputs to the result label
def button_press(ch):

    global equation_text

    equation_text = equation_text + str(ch)

    equation_label.set(equation_text)

# this function calculates the result
def equals():

    global equation_text
    # try except for preventing unintended errors
    try:
        # eval function reads the text and calculate the result and return
        # it as a string
        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError:

        equation_label.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:

        equation_label.set("arithmetic error")

        equation_text = ""

# this function clear the label
def clear():

    global equation_text

    equation_label.set("")

    equation_text = ""

# this function deletes the last character from the label
def delete():
    global equation_text
    equation_text = equation_text[:-1]
    equation_label.set(equation_text)
    equation_text = equation_label.get()

# creating the window
window = Tk()
window.title("Python Calculator from EDK12")
window.geometry("480x630") # the window's height and width

equation_text = ""

equation_label = StringVar()
# creating the result label
label = Label(window, textvariable=equation_label, font=('consolas',20), bg="white", width=24, height=2)
label.pack()
# frame for our buttons to place
frame = Frame(window)
frame.pack()

# the buttons from 1 to 9
btns = []
btns_nmbr = 0

for x in range(0, 3):

    for y in range(0, 3):
        btns_nmbr += 1

        btns.append(Button(frame, text=btns_nmbr, height=4, width=9, font=35,
                           command=lambda btns_nmbr=btns_nmbr: button_press(btns_nmbr)))
        btns[btns_nmbr -1].grid(row=x, column=y)

# the other buttons
button0 = Button(frame, text=0, height=4, width=9, font=35,
                 command=lambda: button_press(0))
button0.grid(row=3, column=0)

plus = Button(frame, text='+', height=4, width=9, font=35,
                 command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35,
                 command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=4, width=9, font=35,
                 command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=4, width=9, font=35,
                 command=lambda: button_press('/'))
divide.grid(row=3, column=3)

equal = Button(frame, text='=', height=4, width=9, font=35,
                 command=equals)
equal.grid(row=3, column=2)

decimal = Button(frame, text='.', height=4, width=9, font=35,
                 command=lambda: button_press('.'))
decimal.grid(row=3, column=1)

clear = Button(frame, text='clear', height=4, width=9, font=35,
                 command=clear)
clear.grid(row = 4, column = 0)

delete = Button(frame, text='delete', height=4, width=9, font=35,
                 command=delete)
delete.grid(row = 4, column = 1)                 
# This code prevents changing the window's height and width
window.resizable(False,False)
# the code for placing the window on the screen and listening for events(inputs)
window.mainloop()