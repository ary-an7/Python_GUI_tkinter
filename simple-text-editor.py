from tkinter import *
from tkinter import filedialog as f

def save():
    file = f.asksaveasfile(initialdir="/home/aryan/Documents/Python/GUI_with-tkinter",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("Python script", ".py"),
                                        ("C++ script", ".cpp"),
                                        ("C script", ".c"),
                                        ("All files", ".*"),
                                    ])
    if file is None:
        return
    filetext = str(text.get(1.0,END))
    file.write(filetext)
    file.close()

window = Tk()
window.geometry("500x500")
window.title("Simple Text editor")
button = Button(text='SAVE',command=save)
button.pack()
text = Text(window)
text.pack()
window.mainloop()