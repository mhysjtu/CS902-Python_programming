from Tkinter import *

class MyApp:
    def __init__(self):
        self.root= Tk()
        Label(self.root,text="Reveal the value here:").pack()

        self.aLabel=Label(self.root,text="")
        self.aLabel.pack()

        self.v1=IntVar()
        self.v2=IntVar()
        self.v3=IntVar()

        Checkbutton(self.root,text="Math",variable=self.v1).pack()
        Checkbutton(self.root,text="Python",variable=self.v2).pack()
        Checkbutton(self.root,text="Chinese",variable=self.v3).pack()

        Button(self.root,text="show value",command=self.showvalue).pack()

        self.root.mainloop()
        
    def showvalue(self):
        self.aLabel["text"]=str(self.v1.get())+str(self.v2.get())+str(self.v3.get())


app = MyApp()
