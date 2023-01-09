from tkinter import *
from time import strftime

root = Tk()
root.geometry("1500x500")
root.resizable(0,0)
root.title("Adarsh's clock")



Label(root,text = "Adarsh project for msc interview", font ='arial 20 bold').pack(side=BOTTOM)
Label(root,text = "DEAR INTERVIEWER,HERE IS YOUR LIVE CLOCK...", font ='arial 30 italic').pack(side=LEFT)
def time():
    string = strftime('%H:%M:%S %p')
    mark.config(text = string)
    mark.after(1000, time)

mark = Label(root,
            font = ('eurostle', 40, 'bold'),
            pady=550,
            foreground = 'pink')

mark.pack(anchor = 'center')
time()

mainloop()