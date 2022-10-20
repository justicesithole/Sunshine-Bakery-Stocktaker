#Creating a stock taking program for a store owner
#Using GUI

from tkinter import *
import datetime

Date = datetime.date.today()

print(Date.strftime("%d %b %Y"))

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
              text = "Enter password for the secret of lengevity"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        #create a second label
        self.pw_lbl = Label(self,
                            text="Password: "
                            ).grid(row = 1, column = 0, sticky = W)

        #create entry widget to accept password
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 1, column = 1, sticky = W)

        #create submit button
        self.submit_bttn = Button(self, text = "Submit", command = self.reveal)
        self.submit_bttn.grid(row = 2, column = 0, sticky = W)

        #create text widget to display message
        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.secret_txt.grid(row = 3, column = 0, columnspan = 2, stick = W)

        #create first button
        self.bttn1 = Button(self, text=("New Stock: ", str(self.bttn_clicks)), command=self.update_count)
        self.bttn1.grid()

        #create seond button
        self.bttn2 = Button(self)
        self.bttn2.configure(text = "Calculate stock", command = self.remove)
        self.bttn2.grid()

    def update_count(self):
        """Increase click count and display new total"""
        self.bttn_clicks += 1
        self.bttn1["text"] = ("New Stock: ", str(self.bttn_clicks))

    def reveal(self):
        """Display message based on password."""
        contents = self.pw_ent.get()
        if contents == "secret":
            message = "Here's the secret to living to 100: live to 99 "\
                      "and then be VERY careful."
        else:
            message = "That's not the correct password, so I can't share "\
                      "the secret with you."

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

