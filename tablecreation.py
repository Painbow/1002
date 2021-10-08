import tkinter
from tkinter import *
from pandastable import Table

def LoadTable(x):

    root = tkinter.Tk()
    root.title('List of Carparks')
    frame = tkinter.Frame(root)
    root.geometry('1920x1080')
    frame.pack(fill=BOTH, expand=1)
    pt = Table(frame, dataframe=x, showstatusbar=True)
    pt.show()
    root.mainloop()