from tkinter import Tk, Label, Button, Entry, filedialog, messagebox
import os
import shutil


class Window:
    targetDir = ""
    destineDir = ""
    targetExt = ""
    target = ""
    destination = ""

    def Reset(self):
        self.targetDir = ""
        self.destineDir = ""
        self.targetExt = ""
        self.target = ""
        self.destination = ""

    def SelectTargetDir(self):
        self.targetDir = filedialog.askdirectory()
        messagebox.showinfo(
            title="Target Directory Selected",
            message=f"You have selected { self.targetDir }"
        )

    def SelectDestineDir(self):
        self.destineDir = filedialog.askdirectory()
        messagebox.showinfo(
            title="Destination Directory Selected",
            message=f"You have selected { self.destineDir }"
        )

    def Script(self):
        try:
            self.targetExt = str(self.entTargetExt.get())

            for path, root, files in os.walk(self.targetDir):
                for f in files:
                    if f.endswith(self.targetExt):
                        self.target = f"{ self.targetDir }/{ f }"
                        self.destination = f"{ self.destineDir }/{ f }"
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


root = Tk()
gui = Window(root)
root.mainloop()
