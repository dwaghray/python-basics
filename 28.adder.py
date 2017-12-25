# creates a GUI that takes two numbers as input and adds them together

from tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.lbl1 = Label(self, text="Enter two numbers")
        self.lbl1.grid()
        self.ent1 = Entry(self, width=30)
        self.ent1.grid()
        self.ent2 = Entry(self, width=30)
        self.ent2.grid()
        self.lbl2 = Label(self, text="The sum: ")
        self.lbl2.grid()
        self.bttn1 = Button(self, text = "Add Numbers", command = self.adder)
        self.bttn1.grid()

    def adder(self):
        try:
            add = (int(self.ent1.get())) + (int(self.ent2.get()))
            self.lbl2["text"] = "The sum: " + str(add)
            self.ent1.delete(0, END)
            self.ent2.delete(0, END)
        except:
            self.lbl2["text"] = "Error: invalid value"
            self.ent1.delete(0, END)
            self.ent2.delete(0, END)


# main
root = Tk()
root.title("Simple Adder")
root.geometry("400x200")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()
