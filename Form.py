from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E

class TransportManager:

    def __init__(self, master):
        self.master = master
        master.title("Transport Manager")

        self.total = 0
        self.entered_number = 0

        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="Total:")


        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)

        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.reset_button.grid(row=2, column=2, sticky=W+E)
        self.order_row()


    def order_row(self):
        self.truck_num = self.text_box()
        self.date = self.text_box()
        self.gc_num = self.gc_num()

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else: # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

    def text_box(self, validate=None):
        if validate:
            vcmd = self.master.register(validate) # we have to wrap the command
            return Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        return Entry(master)


root = Tk()
my_gui = TransportManager(root)
root.mainloop()