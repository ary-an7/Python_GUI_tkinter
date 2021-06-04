from tkinter import *
from tkinter.ttk import *
import time

def start():
    completion = 100
    init = 0
    speed = 1
    while(init<completion):
        time.sleep(0.05)
        bar['value']+=(speed/completion)*100
        init+=speed
        percent.set(str(int((init/completion)*100))+"%")
        text.set(str(init)+"/"+str(completion)+"% Completed")
        window.update_idletasks()

window = Tk()
window.title("Progress bar Example")
percent = StringVar()
text = StringVar()

bar = Progressbar(window,orient=HORIZONTAL,length=500)
bar.pack(pady=10)

percentLabel = Label(window,textvariable=percent).pack()
taskLabel = Label(window,textvariable=text).pack()

button = Button(window,text="START",command=start).pack()

window.mainloop()