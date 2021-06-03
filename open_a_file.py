from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="/home/aryan/Downloads",
                                          title="Open file okay?",
                                          filetypes= (("text files","*.txt"),
                                          ("all files","*.*")))
    file = open(filepath,'r')
    print(file.read())
    file.close()

window = Tk()
window.geometry("500x200")
window.title("Open a file")
label=Label(window,
            text='Click to open a file',
            font=('Arial',20,'italic'),
            padx=0,pady=20,
            compound='bottom')
button = Button(text="Open",
                font=('Roboto',15,'bold'),
                command=openFile,
                padx=30,pady=15,
                activeforeground='green')
#this button will open the file in the terminal of your editor
button.pack()
label.pack()
window.mainloop()