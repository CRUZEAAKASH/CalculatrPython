import parser
from tkinter import *

window = Tk()
window.title("Calcualator")

# Get the user Inpit and display it in the textbox
i = 0


# Display the input in the textbox
def get_variables(num):
    global i
    display.insert(i, num)
    i += 1


# Clear all the input present in textbox
def clear_all():
    global i
    display.delete(0, i)
    print(i)


# Clearing last character
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "Error")


# Display Operator
def operator(opr):
    global i
    i += len(opr)
    display.insert(i, opr)


# Doing Calculations
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")


# Adding textbox
display = Entry(window)
display.grid(row=0, columnspan=6, sticky=W + E)

# Adding Buttons
Button(window, text="1", command=lambda: get_variables(1)).grid(row=1, column=0)
Button(window, text="2", command=lambda: get_variables(2)).grid(row=1, column=1)
Button(window, text="3", command=lambda: get_variables(3)).grid(row=1, column=2)

Button(window, text="4", command=lambda: get_variables(4)).grid(row=2, column=0)
Button(window, text="5", command=lambda: get_variables(5)).grid(row=2, column=1)
Button(window, text="6", command=lambda: get_variables(6)).grid(row=2, column=2)

Button(window, text="7", command=lambda: get_variables(7)).grid(row=3, column=0)
Button(window, text="8", command=lambda: get_variables(8)).grid(row=3, column=1)
Button(window, text="9", command=lambda: get_variables(9)).grid(row=3, column=2)

Button(window, text="AC", command=lambda: clear_all()).grid(row=4, column=0)
Button(window, text="0", command=lambda: get_variables(0)).grid(row=4, column=1)
Button(window, text="=", command=lambda: calculate()).grid(row=4, column=2)

Button(window, text="+", command=lambda: operator("+")).grid(row=1, column=3)
Button(window, text="-", command=lambda: operator("-")).grid(row=2, column=3)
Button(window, text="*", command=lambda: operator("*")).grid(row=3, column=3)
Button(window, text="/", command=lambda: operator("/")).grid(row=4, column=3)

Button(window, text="pi", command=lambda: operator("3.14")).grid(row=1, column=4)
Button(window, text="%", command=lambda: operator("%")).grid(row=2, column=4)
Button(window, text="(", command=lambda: operator("(")).grid(row=3, column=4)
Button(window, text="exp", command=lambda: operator("**")).grid(row=4, column=4)

Button(window, text="<-", command=lambda: undo()).grid(row=1, column=5)
Button(window, text="x!").grid(row=2, column=5)
Button(window, text=")", command=lambda: operator(")")).grid(row=3, column=5)
Button(window, text="^2", command=lambda: operator("**2")).grid(row=4, column=5)

window.mainloop()
