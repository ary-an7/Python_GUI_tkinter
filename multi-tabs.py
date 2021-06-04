from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Multiple Tabs eg")

notebook = ttk.Notebook(window) 

tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)
tab4 = Frame(notebook)


notebook.add(tab1,text="Tab 1")
notebook.add(tab2,text="Tab 2")
notebook.add(tab3,text="Tab 3")
notebook.add(tab4,text="Tab 4")

notebook.pack(expand=True,fill="both") 
Label(tab1,text="Hi This is TAB1",width=50,height=25,bg='white',font=('Roboto',10)).pack()
Label(tab2,text="This is TAB2",width=50,height=25,bg='red',font=('Roboto',10)).pack()
Label(tab3,text="This is TAB3",width=50,height=25,bg='green',font=('Roboto',10)).pack()
Label(tab4,text="This is TAB4",width=50,height=25,bg='blue',font=('Roboto',10)).pack()

window.mainloop()