import Tkinter as Tk
import tkFileDialog

root = Tk.Tk()
root.title("File Extension Mover")
root.geometry("1280x720")

global folder
folder = ""


def browse():
    dirname = tkFileDialog.askdirectory(
        parent=root,
        initialdir="/",
        title='Please select a directory'
    )
    global folder
    folder = dirname


btn1 = Tk.Button(
    root,
    text="Open File Explorer",
    command=browse
)
btn1.place(x=0, y=0)

txt1 = Tk.Label(
    root,
    text=str(folder)
)
txt1.place(x=0, y=10)

Tk.mainloop()
