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
        self.cloud = None
        self.at_btn = None
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
        self.subFont = font.Font(
                    family="Microsoft JhengHei",
                    size=10,
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
    
        # Attachment Section
        self.image = PhotoImage(file="./img/attacth_outerbox.png")
        image_id = self.canvas.create_image(170, 130, anchor=NW, image=self.image)
        image_id_x = 170
        #image_id_y = 130
        image_id_width = self.image.width()
        # Cloud
        self.cloud = PhotoImage(file="./img/cloud.png")
        cloud_width = self.cloud.width()
        cloud_height = self.cloud.height()
        #cloud position
        cloud_x = image_id_x + (image_id_width - cloud_width) // 2
        cloud_id = self.canvas.create_image(cloud_x, 150, anchor=NW, image=self.cloud)
         #text
        # Create a label with Manrope font
        sub_label = Label(self.canvas, text="Browse and chose the dataset you want to upload from your computer.JSON files only.", font=self.subFont, bg='white', fg='#191D23')
        sub_label.pack(pady=20, padx=0)
        sub_width = sub_label.winfo_reqwidth()
        sub_textx = image_id_x + (image_id_width - sub_width) // 2
        self.canvas.create_window(sub_textx, 200, window=sub_label, anchor=NW)
        # Pack the canvas to make it visible
        self.canvas.pack(fill=BOTH, expand=YES)

# You can include other methods or modify the existing ones based on your needs
