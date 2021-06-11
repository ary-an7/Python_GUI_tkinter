from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("--%A--")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000,update)


window = Tk()
window.title("TIME and DATE")

date_label = Label(window,font=("Roboto",25,'italic'))
date_label.pack()

time_label = Label(window,font=("Roboto",32,'italic'),fg="green",bg="black")
time_label.pack()

day_label = Label(window,font=("Roboto",25,'italic'))
day_label.pack()

update()

window.mainloop()