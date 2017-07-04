try:
    from Tkinter import *
    from ttk import *
except ImportError:  # Python 3
    from tkinter import *
    from tkinter.ttk import *


class App(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N,S,W,E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def CreateUI(self):
        tv = Treeview(self)
        self.treeview = tv

        tv['columns'] = ('gcNum', 'truckNum', 'client', 'loading', 'received', 'rate', 'amount')
        self.add_column_and_heading('#0', 'Date')
        self.add_column_and_heading('gcNum', 'GC No.')
        self.add_column_and_heading('truckNum', 'Truck No.')
        self.add_column_and_heading('client', 'Client')
        self.add_column_and_heading('loading', 'Loaded Quantity')
        self.add_column_and_heading('received', 'Received Quantity')
        self.add_column_and_heading('rate', 'Rate')
        self.add_column_and_heading('amount', 'Amount')
        tv.grid(sticky = (N,S,W,E))
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def add_column_and_heading(self, column_name, heading):
        self.treeview.column(column_name, anchor='center', width=100)
        self.treeview.heading(column_name, text=heading)

    def LoadTable(self):
        self.treeview.insert('', 'end', text="First", values=('10:00',
                             '10:10', 'Ok'))
        self.treeview.insert('', 'end', text="First", values=('10:00',
                             '10:10', 'Ok'))
        self.treeview.insert('', 'end', text="First", values=('10:00',
                             '10:10', 'Ok'))
        self.treeview.insert('', 'end', text="First", values=('10:00',
                             '10:10', 'Ok'))
        self.treeview.insert('', 'end', text="First", values=('10:00',
                             '10:10', 'Ok'))

def main():
    root = Tk()
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()