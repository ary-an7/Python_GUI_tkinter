from tkinter import *
from tkinter import colorchooser

def click():
    color = colorchooser.askcolor() 
    colorHex = color[1]    
    window.config(bg=colorHex) 

window = Tk()
window.geometry("800x400")
window.title("HEX Generator/Background changer")
label=Label(window,
            text='Press the button to change background or select hex code',
            font=('Arial',20,'italic'),
            padx=0,pady=20,
            compound='bottom')
button = Button(text="Press",
                font=('Roboto',15,'bold'),
                command=click,
                padx=30,pady=15,
                activeforeground='red',
                        )
button.pack()
label.pack()
window.mainloop()