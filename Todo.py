def submit():
    todo= []
    for i in listbox.curselection():
        todo.insert(i,listbox.get(i))

    print("You have TO-DO:\n ")
    for i in todo:
        print(i)

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)

    listbox.config(height=listbox.size())

from tkinter import *


window = Tk()
window.geometry("400x500")
window.title("TASKER or TODO")
window.config(background='grey')


listbox = Listbox(window,
                  bg="#010101",
                  font=("Times New Roman",25),
                  width=12,
                  fg="green",   
                  selectmode=MULTIPLE)
listbox.pack()


#predefining some example tasks
listbox.insert(1,"code in python")
listbox.insert(2,"play basketball")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

frame = Frame(window)
frame.pack()
#a submit button to submit the list after selecting the todos
submitButton = Button(frame,text="submit",command=submit)
submitButton.pack(side=LEFT)
#an add button to add the todos in the list by typing in the textbox
addButton = Button(frame,text="add",command=add)
addButton.pack(side=LEFT)
#delete a task after selecting it and clicking on delete
deleteButton = Button(frame,text="delete",command=delete)
deleteButton.pack(side=LEFT)

window.mainloop()


