from tkinter import *
from tkinter import font,ttk,messagebox, filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

class Results(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.master = master
        self.mainFont = None
        self.image = None
        self.cloud = None
        self.at_btn = None
        self.create_widgets()

    def font_setup(self):
        # Define Our Font
        self.mainFont = font.Font(
            family="Microsoft JhengHei Light",
            size=20,
            weight="normal",
            slant="roman",
            underline=0,
            overstrike=0)
        self.subFont = font.Font(
                    family="Dubai Light",
                    size=18,
                    weight="normal",
                    slant="roman",
                    underline=0,
                    overstrike=0)

    def create_widgets(self):
        # Call font_setup to load the font
        self.font_setup()
        self.canvas = Canvas(self, bg='white', highlightthickness=0)
        # Create a label with Manrope font
        label = Label(self.canvas, text="TBD", font=self.mainFont, bg='white', fg='#191D23')
        label.pack(pady=20, side=TOP, padx=0)
        # Create a window on the canvas and add the label to it
        self.canvas.create_window(200, 100, window=label, anchor=NW)
    
