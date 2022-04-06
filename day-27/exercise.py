import tkinter

import Playground

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)


def button_click():
    my_label.config(text=input_box.get())


# Label
my_label = tkinter.Label(text=f"It is a Label", font=("Arial", 11, "bold"))
my_label.grid(row=1, column=1)

my_label.config(text="new text")

my_button = tkinter.Button(text="Click Me", command=button_click)
my_button.grid(row=2, column=2)

new_button = tkinter.Button(text="New Button")
new_button.grid(row=1, column=3)

input_box = tkinter.Entry()
input_box.grid(row=3, column=4)

window.mainloop()