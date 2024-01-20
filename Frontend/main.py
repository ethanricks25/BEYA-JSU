# main.py
from tkinter import *
from tkinter import ttk
from welcome import WelcomePage
from inputStats import InputDataPage

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("PRISM")
        self.geometry("1000x700")
        self.configure(background='white')
        self.minsize(1000, 700)

        # Create a Notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=BOTH, expand=YES)

        # Create welcome page
        welcome_page = WelcomePage(self.notebook)
        welcome_page.pack(fill=BOTH, expand=YES)
        self.notebook.add(welcome_page, text="Welcome")

        # Create input data page
        input_data_page = InputDataPage(self.notebook)
        input_data_page.pack(fill=BOTH, expand=YES)
        self.notebook.add(input_data_page, text="Input Data",state='disabled')

        self.mainloop()

if __name__ == "__main__":
    app = MainApp()
