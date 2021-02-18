# Python 3.7.3

import os
import shutil
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox


class Window:
    # Declaring variables
    targetDir = ""
    destineDir = ""
    targetExt = ""
    target = ""
    destination = ""

    # Sets variables to null
    def Reset(self):
        self.targetDir = ""
        self.destineDir = ""
        self.targetExt = ""
        self.target = ""
        self.destination = ""

    # Called when self.btnTargetDir is pressed
    def SelectTargetDir(self):
        # Path to target directory
        self.targetDir = filedialog.askdirectory()
        messagebox.showinfo(
            title="Target Directory Selected",
            message=f"You have selected { self.targetDir }"
        )

    # Called when self.btnDestineDir is pressed
    def SelectDestineDir(self):
        # Path to destination directory
        self.destineDir = filedialog.askdirectory()
        messagebox.showinfo(
            title="Destination Directory Selected",
            message=f"You have selected { self.destineDir }"
        )

    # Called when self.btnRunScript is pressed
    def Script(self):
        # Catches any errors when running script
        try:
            # Target extension in format of .*
            self.targetExt = str(self.entTargetExt.get())

            # Returns the target directory path, sub directories, and files
            for path, root, files in os.walk(self.targetDir):
                # Iterates through files in target directory
                for f in files:
                    # Checks if the end of the file matches the
                    # targeted extension.
                    if f.endswith(self.targetExt):
                        # Stores target file's path
                        self.target = f"{ self.targetDir }/{ f }"
                        # Stores destination path for file
                        self.destination = f"{ self.destineDir }/{ f }"
                        # Moves target file to destination directory
                        shutil.move(self.target, self.destination)

            messagebox.showinfo(
                title="Files Moved",
                message=f"Your { self.targetExt } files in { self.targetDir }" +
                        f" have been successfully moved to { self.destineDir }!"
            )

            self.Reset()
        except:
            messagebox.showerror(
                title="Unable To Move Files",
                message="An error has occured whilst trying to move your " +
                        "files. Please re-select your target extension, " +
                        "target and destination directory and try again!"
            )

            self.Reset()

    def __init__(self, master):
        self.master = master

        master.title("File Extension Mover")

        # tkinter label widget
        self.lblTitle = Label(
            master,
            text="FILE EXTENSION MOVER"
        )
        self.lblTitle.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="NESW",
            pady=(0, 10),
            padx=2.5
        )

        # tkinter button widget
        self.btnTargetDir = Button(
            master,
            text="Select Target Folder",
            command=self.SelectTargetDir
        )
        self.btnTargetDir.grid(
            row=1,
            column=0,
            sticky="NESW",
            pady=(0, 5),
            padx=2.5
        )

        # tkinter button widget
        self.btnDestineDir = Button(
            master,
            text="Select Destination Folder",
            command=self.SelectDestineDir
        )
        self.btnDestineDir.grid(
            row=2,
            column=0,
            sticky="NESW",
            pady=(0, 5),
            padx=2.5
        )

        # tkinter label widget
        self.lblTargetExt = Label(
            master,
            text="Target Extension:"
        )
        self.lblTargetExt.grid(
            row=3,
            column=0,
            sticky="W",
            padx=2.5
        )

        # tkinter text entry widget
        self.entTargetExt = Entry(
            master
        )
        self.entTargetExt.grid(
            row=4,
            column=0,
            sticky="NESW",
            pady=(0, 5),
            padx=2.5
        )

        # tkinter button widget
        self.btnRunScript = Button(
            master,
            text="Move Files",
            command=self.Script
        )
        self.btnRunScript.grid(
            row=5,
            column=0,
            sticky="NESW",
            pady=(0, 2.5),
            padx=2.5
        )


if __name__ == "__main__":
    root = Tk()
    gui = Window(root)
    root.mainloop()
