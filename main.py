import tkinter as Tk
from tkinter import filedialog
from tkinter import ttk
import os
import shutil


root = Tk.Tk()
root.title("File Extension Mover")


def submitExtension():
    txt2.configure(text="Targeted extension: " + str(ent1.get()))


def targetFolder():
    global targetDir
    targetDir = filedialog.askdirectory()
    txt3.configure(text="Targeted folder: " + targetDir)


def destinationFolder():
    global destinationDir
    destinationDir = filedialog.askdirectory()
    txt4.configure(text="Destination folder: " + destinationDir)


def startScript():
    for path, root, files in os.walk(targetDir):
        for x in files:
            if x.endswith(str(ent1.get())):
                source = targetDir + "/" + x
                destination = destinationDir + "/" + x
                shutil.move(source, destination)


txt1 = Tk.Label(
    root,
    text="Choose the file extension you would like to target e.g. .png or .jpg"
)
txt1.pack()

ent1 = Tk.Entry(root)
ent1.pack()

btn1 = ttk.Button(
    root,
    text="Submit extension",
    command=submitExtension
)
btn1.pack()

btn2 = Tk.Button(
    root,
    text="Choose target folder",
    command=targetFolder
)
btn2.pack()

btn3 = Tk.Button(
    root,
    text="Choose destination folder",
    command=destinationFolder
)
btn3.pack()

txt2 = Tk.Label(
    root,
    text="Targeted extension: "
)
txt2.pack()

txt3 = Tk.Label(
    root,
    text="Targeted folder: "
)
txt3.pack()

txt4 = Tk.Label(
    root,
    text="Destination folder: "
)
txt4.pack()

btn4 = Tk.Button(
    root,
    text="Move files",
    command=startScript
)
btn4.pack()

Tk.mainloop()
