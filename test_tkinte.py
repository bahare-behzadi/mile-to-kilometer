from tkinter import *


def calculate():
    km_distance = float(input_distance.get()) * 1.62137
    km_value.config(text=f"{km_distance}")


window = Tk()
window.title("This program convert Miles to Kilometer")
window.bell()
window.config(padx=30, pady=30)
input_distance = Entry(width=7)
input_distance.grid(column=2, row=1)
mile_label = Label(text="Miles")
mile_label.grid(column=3, row=1)
is_label = Label(text="is equal to")
is_label.grid(column=1, row=2)
km_value = Label(text="0")
km_value.grid(column=2, row=2)
km = Label(text="KM")
km.grid(column=3, row=2)
cla_button = Button(text="Calculate", command=calculate)
cla_button.grid(column=2, row=3)

window.mainloop()
