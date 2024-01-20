from tkinter import *
from tkinter import font
from tkinter import ttk

class InputDataPage(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.master = master
        self.mainFont = None
        self.create_widgets()

    def font_setup(self):
        # Define Our Font
        self.mainFont = font.Font(
            family="Microsoft JhengHei",
            size=20,
            weight="normal",
            slant="roman",
            underline=0,
            overstrike=0)

        # Define Our Font
        mediumFont = font.Font(
            family="Helvetica",
            size=24,
            weight="normal",
            slant="italic",
            underline=1,
            overstrike=0)

    def create_widgets(self):
        # Call font_setup to load the font
        self.font_setup()

        canvas = Canvas(self, bg='white', highlightthickness=0)
        canvas.pack(fill=BOTH, expand=YES)

        # Create a label with Manrope font
        label = Label(self, text="Hello, Manrope!", font=self.mainFont, bg='white', fg='#191D23')
        label.pack(pady=20, side=TOP)

# You can include other methods or modify the existing ones based on your needs
