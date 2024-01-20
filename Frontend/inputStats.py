from tkinter import *
from tkinter import font
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont

class InputDataPage(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.master = master
        self.mainFont = None
        self.image = None
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

    def create_widgets(self):
        # Call font_setup to load the font
        self.font_setup()
        self.canvas = Canvas(self, bg='white', highlightthickness=0)
        # Create a label with Manrope font
        label = Label(self.canvas, text="Input Dataset", font=self.mainFont, bg='white', fg='#191D23')
        label.pack(pady=20, side=TOP, padx=0)
        # Create a window on the canvas and add the label to it
        self.canvas.create_window(200, 100, window=label, anchor=NW)
    
        # Load an image
        self.image = PhotoImage(file="./img/attacth_outerbox.png")
        # Create an image on the canvas
        image_id = self.canvas.create_image(170, 130, anchor=NW, image=self.image)

        # Pack the canvas to make it visible
        self.canvas.pack(fill=BOTH, expand=YES)

# You can include other methods or modify the existing ones based on your needs