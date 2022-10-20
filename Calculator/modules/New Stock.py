#Creating a stock taking program for a store owner
#Using GUI

from tkinter import *

import os

current_dir = os.getcwd()

stock_file = open(os.path.join(current_dir, "files\\new_stock.txt"), "w")
stock_file.write("Hello World")
stock_file.close()


class Application(Frame):
    """A GUI application for stock taking"""

    def __init__(self, master):
        """Initialize the Frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create__widgets()

    def create__widgets(self):
        """Create the widgets for the app."""

        #create instruction label
        Label(self,
              text = "Enter the Amount of Stock you purchased"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)


        #Stock input fields
        Label(self,
              text = "Floor: "
              ).grid(row = 1, column = 0, sticky = W)
        self.floor = Entry(self)
        self.floor.grid(row = 1, column = 1, sticky = W)

        Label(self,
              text = "Sugar: "
              ).grid(row = 2, column = 0, sticky = W)
        self.sugar = Entry(self)
        self.sugar.grid(row = 2, column = 1, sticky = W)

        Label(self,
              text = "Fish Oil: "
              ).grid(row = 3, column = 0, sticky = W)
        self.fish_oil = Entry(self)
        self.fish_oil.grid(row = 3, column = 1, sticky = W)

        Label(self,
              text = "Milk: "
              ).grid(row = 4, column = 0, sticky = W)
        self.milk = Entry(self)
        self.milk.grid(row = 4, column = 1, sticky = W)

        #The submit button
        Button(self,
               text = "Submit", command = self.reveal
               ).grid(row = 5, column = 0, sticky = W)

        #create text widget to display message
        self.secret_txt = Text(self, width = 35, height = 15, wrap = WORD)
        self.secret_txt.grid(row = 6, column = 0, columnspan = 2, stick = W)

    def update_count(self):
        """Increase click count and display new total"""
        self.bttn_clicks += 1
        self.bttn1["text"] = ("New Stock: ", str(self.bttn_clicks))

    def reveal(self):
        """Display message based on password."""
        Stock = ["Floor", "Sugar", "Fish Oil", "Milk"]
        contents = [self.floor.get(), self.sugar.get(), self.fish_oil.get(), self.milk.get()]
        message = "Your Items that you Purchased\n\n"
        for item in range(4):
            message += str(item + 1)
            message += ") "
            message += str(Stock[item])
            message += ": "
            message += str(contents[item])
            message += "\n\n"

        current_dir = os.getcwd()
        stock_file = open(os.path.join(current_dir, "files\\new_stock.txt"), "w")
        stock_file.write(message)
        stock_file.close()
        
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)

    def remove(self):
        self.bttn2.grid_remove()

#main
root = Tk()
root.title("SUNSHINE BAKERY STOCK TAKER")
root.geometry("800x400")

app = Application(root)

root.mainloop()

    
"""
#create the root window
root = Tk()

#modify the window
root.title("SUNSHINE BAKERY STOCK TAKER")
root.geometry("200x100")

#creating a frame in the window to hold other widgets
app = Frame(root)
app.grid()

#create a label in the frame
lbl = Label(app, text = "I'm a label!")
lbl.grid()

#create a button in the frame
bttn1 = Button(app, text = "New Stock")
bttn1.grid()

bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text = "Take Stock")

#kick off the window's event loop
root.mainloop()
"""

