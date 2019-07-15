from tkinter import *

window = Tk()
window.title("Calcualator")

# Get the user INpit and display it in the textbox
i = 0


def get_variables(num):
    global i
    display.insert(i, num)
    i += 1


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

Button(window, text="AC").grid(row=4, column=0)
Button(window, text="0", command=lambda: get_variables(10)).grid(row=4, column=1)
Button(window, text="=").grid(row=4, column=2)

Button(window, text="+").grid(row=1, column=3)
Button(window, text="-").grid(row=2, column=3)
Button(window, text="*").grid(row=3, column=3)
Button(window, text="/").grid(row=4, column=3)

Button(window, text="pi").grid(row=1, column=4)
Button(window, text="%").grid(row=2, column=4)
Button(window, text="(").grid(row=3, column=4)
Button(window, text="exp").grid(row=4, column=4)

Button(window, text="<-").grid(row=1, column=5)
Button(window, text="x!").grid(row=2, column=5)
Button(window, text=")").grid(row=3, column=5)
Button(window, text="^2").grid(row=4, column=5)

window.mainloop()
