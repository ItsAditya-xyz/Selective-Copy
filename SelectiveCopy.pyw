import tkinter as tk
from tkinter import filedialog
from tkinter import *
import time
import tkinter.messagebox as msgbx
import tkinter.ttk as ttk
import shutil
import webbrowser
source=""
import os
destination=''
class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Selective Copy")
        self.geometry("1024x480")
        self.resizable(0,0)

        self.toCopy=tk.BooleanVar()
        self.toCopy.set(True)

        icon=PhotoImage(file=os.path.join(os.getcwd(),"smile.png"))
        self.iconphoto(False, icon)

#Labeling goes here
        frame=tk.Frame(self)
        frame.pack(fill=tk.BOTH)
        self.label1=ttk.Label(frame,width=0)
        self.label1.pack(side=tk.LEFT, padx=5, pady=5)
        self.isSubfolderTOO=tk.BooleanVar()


        self.label=ttk.Label(frame, text="Choose Source Folder:")
        self.label.pack(fill=tk.BOTH,side=tk.LEFT, expand=False, padx=0, pady=20)



        chooseSbutton = ttk.Button(frame, text="Select Source", command=self.chooseSource)
        chooseSbutton.pack(side=tk.RIGHT, padx=120, pady=20)

        self.source = tk.StringVar()
        SourceBox = ttk.Entry(frame, text=self.source, width=80)
        SourceBox.pack(side=tk.RIGHT, padx=0, pady=20)

        frame0=tk.Frame(self)
        frame0.pack(fill=tk.BOTH)
        sub = ttk.Checkbutton(frame0, text="Include subfolders?", variable=self.isSubfolderTOO)
        sub.pack(side=tk.LEFT, padx=449, pady=10)

 #For destination thingy
        frame2 = tk.Frame(self)
        frame2.pack(fill=tk.BOTH)

        self.promptD=ttk.Label(frame2, text="Choose Destination Folder:")
        self.promptD.pack(fill=tk.BOTH,side=tk.LEFT, expand= False, padx= 13, pady=25)

        chooseDbutton = ttk.Button(frame2, text="Select Destination", command=self.chooseDestination)
        chooseDbutton.pack(side=tk.RIGHT, padx=100, pady=25)

        self.destination = tk.StringVar()
        DestBox = ttk.Entry(frame2, text=self.destination, width=80)
        DestBox.pack(side=tk.RIGHT, padx=20, pady=25)


##Check Buttons along with their Variables
        frame3 = tk.Frame(self)
        frame3.pack(fill=tk.BOTH)

        self.chmp3=tk.BooleanVar()
        self.chpdf=tk.BooleanVar()
        self.chpng=tk.BooleanVar()
        self.chjpeg=tk.BooleanVar()
        self.chzip=tk.BooleanVar()
        self.chexe=tk.BooleanVar()
        self.chCustomExt=tk.BooleanVar()


        promptEx=ttk.Label(frame3, text="Choose Extension(s):")
        promptEx.pack(fill=tk.BOTH, side= tk.LEFT, padx=10,pady=45)

        mp3= ttk.Checkbutton(frame3,text=".mp3", variable=self.chmp3)
        mp3.pack(side=tk.LEFT, padx= 20, pady=50)

        pdf=ttk.Checkbutton(frame3, text=".pdf", variable=self.chpdf)
        pdf.pack(side=tk.LEFT, padx=22, pady =50)

        png=ttk.Checkbutton(frame3, text=".png", variable=self.chpng)
        png.pack(side=tk.LEFT, padx= 24, pady=50)

        jpeg=ttk.Checkbutton(frame3, text=".jpeg", variable=self.chjpeg)
        jpeg.pack(side=tk.LEFT,padx=26,pady=50)

        zip=ttk.Checkbutton(frame3, text=".zip", variable=self.chzip)
        zip.pack(side=tk.LEFT, padx=28,pady=50)

        exe=ttk.Checkbutton(frame3, text=".exe", variable=self.chexe)
        exe.pack(side=tk.LEFT, padx=30, pady=50)

        customExtension=ttk.Checkbutton(frame3, text="Custom Extension", variable=self.chCustomExt, command=self.cstExt)
        customExtension.pack(side=tk.LEFT, padx=40, pady=50)



        frame4=tk.Frame(self)
        frame4.pack(fill=tk.BOTH)


        self.promtext=ttk.Label(frame4, text="OR type extensions separated by commas:",state=tk.DISABLED)
        self.promtext.pack(fill=tk.BOTH,side=tk.LEFT, padx=10,pady=10)

        self.exentry=tk.StringVar()
        self.extEntry=ttk.Entry(frame4,text=self.exentry, width=80,state=tk.DISABLED)
        self.extEntry.pack(side=tk.LEFT, padx=22,pady=10)

        frame5= tk.Frame(self)
        frame5.pack(fill=tk.BOTH)

        copy=ttk.Button(frame5, text="Copy",command=self.copy)
        copy.pack(side=tk.LEFT,padx=200,pady= 20)
        move=ttk.Button(frame5,text="Move",command=self.move)
        move.pack(side=tk.LEFT,padx=220,pady=20)

        link1 = Label(self, text="-by Aditya", fg="green", cursor="hand2")
        link1.pack(side=tk .RIGHT,padx=9,pady=40)
        link1.bind("<Button-1>", lambda e: webbrowser.open_new("https://twitter.com/AdityaGameDev"))

    def chooseSource(self):
        root=tk.Tk()
        root.withdraw()
        source= filedialog.askdirectory()
        self.source.set(source)

    def chooseDestination(self):
        root=tk.Tk()
        root.withdraw()
        destination=filedialog.askdirectory()
        self.destination.set(destination)
    def cstExt(self):
        if self.chCustomExt.get():
            self.promtext.configure(state=tk.NORMAL)
            self.extEntry.configure(state=tk.NORMAL)
        else:
            self.promtext.configure(state=tk.DISABLED)
            self.extEntry.configure(state=tk.DISABLED)
    def copy(self):
        s=''
        count={}

        #creating list of extensions
        extensions=[]
        if self.chmp3.get():
            extensions.append(".mp3")
        if self.chpdf.get():
            extensions.append(".pdf")
        if self.chjpeg.get():
            extensions.append(".jpeg")
        if self.chexe.get():
            extensions.append(".exe")
        if self.chpng.get():
            extensions.append(".png")
        if self.chzip.get():
            extensions.append(".zip")
        if self.chCustomExt.get():
            ss=""
            s=self.exentry.get()
            if s!='':
                for c in s:
                    if not c==' ':
                        ss+=c
                cextensions=ss.split(',')
                for ext in cextensions:
                    extensions.append(ext)
        for num in extensions:
            count[num]=0
        if not os.path.isdir(self.source.get()):
            msgbx.showerror("Invalid Source","No such Source Found. Select a Valid Source Folder")
        elif not os.path.isdir(self.destination.get()):
            msgbx.showerror("Invalid Destination","No such Destination Found. Select a Valid Destination Folder ")
        elif len(extensions)==0:
            msgbx.showwarning("Select Extension","Select atleast one extension")
        else:
            try:
                if self.isSubfolderTOO.get():
                    t1=time.time()
                    for folders, subfolders, files in os.walk(self.source.get()):
                        for file in files:
                            for extension in extensions:
                                if file.endswith(extension):
                                    count[extension] += 1
                                    shutil.copy(os.path.join(folders, file), self.destination.get())
                    t = time.time() - t1
                    msg = 'Files have been Copied. Number of files found:\n'
                    for key in count:
                        msg += key + " : " + str(count[key]) + '\n'
                    msg += "\n It took " + str(t) + " seconds to complete the operation"
                    msgbx.showinfo("Done!", msg)
                    os.startfile(self.destination.get())

                else:
                    t1=time.time()
                    files=os.listdir(self.source.get())
                    for file in files:
                        if os.path.isfile(os.path.join(self.source.get(),file)):
                            for extension in extensions:
                                if file.endswith(extension):
                                    count[extension] += 1
                                    shutil.copy(os.path.join(self.source.get(),file),self.destination.get())
                    t=time.time()-t1
                    msg='Files have been Copied. Number of files found:\n'
                    for key in count:
                        msg+=key+" : "+str(count[key])+'\n'
                    msg+="\n It took "+str(t)+" seconds to complete the operation"
                    msgbx.showinfo("Done!",msg)
                    os.startfile(self.destination.get())
            except shutil.Error:
                msgbx.showerror("Error!","It seems that some files of same name already exist in destination folder\n\nTry again! ")
    def move(self):
        s = ''
        count = {}
        extensions = []
        if self.chmp3.get():
            extensions.append(".mp3")
        if self.chpdf.get():
            extensions.append(".pdf")
        if self.chjpeg.get():
            extensions.append(".jpeg")
        if self.chexe.get():
            extensions.append(".exe")
        if self.chpng.get():
            extensions.append(".png")
        if self.chzip.get():
            extensions.append(".zip")
        if self.chCustomExt.get():
            ss = ""
            s = self.exentry.get()
            if s != '':
                for c in s:
                    if not c == ' ':
                        ss += c
                cextensions = ss.split(',')
                for ext in cextensions:
                    extensions.append(ext)
        for num in extensions:
            count[num] = 0
        if not os.path.isdir(self.source.get()):
            msgbx.showerror("Invalid Source", "No such Source Found. Select a Valid Source Folder")
        elif not os.path.isdir(self.destination.get()):
            msgbx.showerror("Invalid Destination", "No such Destination Found. Select a Valid Destination Folder ")
        elif len(extensions) == 0:
            msgbx.showwarning("Select Extension", "Select atleast one extension")
        else:
            try:
                if self.isSubfolderTOO.get():
                    t1 = time.time()
                    for folders, subfolders, files in os.walk(self.source.get()):
                        for file in files:
                            for extension in extensions:
                                if file.endswith(extension):
                                    count[extension] += 1
                                    shutil.move(os.path.join(folders, file), self.destination.get())
                    t = time.time() - t1
                    msg = 'Files have been Moved. Number of files found:\n'
                    for key in count:
                        msg += key + " : " + str(count[key]) + '\n'
                    msg += "\n It took " + str(t) + " seconds to complete the operation"
                    msgbx.showinfo("Done!", msg)
                    os.startfile(self.destination.get())
                else:
                    files = os.listdir(self.source.get())
                    t1 = time.time()
                    for file in files:
                        if os.path.isfile(os.path.join(self.source.get(), file)):
                            for extension in extensions:
                                if file.endswith(extension):
                                    count[extension] += 1
                                    shutil.move(os.path.join(self.source.get(), file), self.destination.get())
                    t = time.time() - t1
                    msg = 'Files have been Moved. Number of files found:\n'
                    for key in count:
                        msg += key + " : " + str(count[key]) + '\n'
                    msg += "\n It took " + str(t) + " seconds to complete the operation"
                    msgbx.showinfo("Done!", msg)
                    os.startfile(self.destination.get())
            except shutil.Error:
                msgbx.showerror("Error!","It seems that some files of same name already exist in destination folder\n\nTry again! ")

if __name__  == "__main__":
    window=Window()
    os.startfile(os.getcwd())
   # window.resizable(0,0)
    window.mainloop()

