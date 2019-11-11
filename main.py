import Tkinter as Tk
import tkFileDialog

root = Tk.Tk()
root.title("File Extension Mover")
root.geometry("1280x720")

global dirname
dirname = ""


def browse():
    global dirname
    dirname = tkFileDialog.askdirectory(
        parent=root,
        initialdir="/",
        title='Please select a directory'
    )


btn1 = Tk.Button(
    root,
    text="Open File Explorer",
    command=browse
)
btn1.place(x=0, y=0)

txt1 = Tk.Label(
    root,
    text="dirname: " + str(dirname)
)
txt1.place(x=50, y=50)

Tk.mainloop()
