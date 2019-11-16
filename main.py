import tkinter as Tk
from tkinter import filedialog
from tkinter import StringVar
import os
import shutil


root = Tk.Tk()
root.title("File Extension Mover")


def submitExtension():
    txt3.configure(text="Targeted Extension: " + str(ent1.get()))


def targetFolder():
    global targetDir
    targetDir = filedialog.askdirectory()
    txt4.configure(text="Targeted Folder: " + targetDir)


def destinationFolder():
    global destinationDir
    destinationDir = filedialog.askdirectory()
    txt5.configure(text="Destination Folder: " + destinationDir)


def startScript():
    for path, root, files in os.walk(targetDir):
        for x in files:
            if x.endswith(str(ent1.get())):
                source = targetDir + "/" + x
                destination = destinationDir + "/" + x
                shutil.move(source, destination)


txt1 = Tk.Label(
    root,
    text="FILE EXTENSION MOVER",
    font=("arial", 32, "bold")
)
txt1.grid(row=0, column=2)

nl1 = Tk.Label(
    root,
    text=" "
)
nl1.grid(row=1, column=2)

txt2 = Tk.Label(
    root,
    text="Enter Target Extension:",
)
txt2.grid(row=2, column=0)

ent1 = Tk.Entry(
    root,
)
ent1.grid(row=2, column=2)

btn1 = Tk.Button(
    root,
    text="Target Extension",
    command=submitExtension,
)
btn1.grid(row=2, column=4)

nl3 = Tk.Label(
    root,
    text=" "
)
nl3.grid(row=3, column=2)

btn2 = Tk.Button(
    root,
    text="Choose Target Folder",
    command=targetFolder
)
btn2.grid(row=4, column=1)

btn3 = Tk.Button(
    root,
    text="Choose Destination Folder",
    command=destinationFolder
)
btn3.grid(row=4, column=3)

nl4 = Tk.Label(
    root,
    text=" "
)
nl4.grid(row=5, column=2)

txt3 = Tk.Label(
    root,
    text="Target Extension: "
)
txt3.grid(row=6, column=2)

txt4 = Tk.Label(
    root,
    text="Target Folder: "
)
txt4.grid(row=7, column=2)

txt5 = Tk.Label(
    root,
    text="Destination Folder: "
)
txt5.grid(row=8, column=2)

nl5 = Tk.Label(
    root,
    text=" "
)
nl5.grid(row=9, column=2)

btn4 = Tk.Button(
    root,
    text="Move Files",
    command=startScript
)
btn4.grid(row=10, column=2)

Tk.mainloop()
