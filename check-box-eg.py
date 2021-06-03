from tkinter import *

def display():
    if(x.get()):
        print("YES")   #if checked print YES
    else:
        print("NO")  #if clicked print NO

window = Tk()
window.geometry("500x200")
window.title("Checkbox trial")
x = IntVar()


checkbox = Checkbutton(       window,
                              text='I lOVE CODING',
                              variable=x,
                              onvalue=True,
                              offvalue=False,
                              command=display,
                              font=('Times New Roman',30),
                              fg='#ff0000',
                              bg='#000000',
                              activeforeground='#00ff00',
                              activebackground='#000000',
                              padx=50,
                              pady=50,
                              width=200,
                              height=50,
                              anchor='w',
                              compound='left')
checkbox.pack()

window.mainloop()