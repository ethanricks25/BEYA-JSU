from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import filedialog  # Import filedialog module
from PIL import Image, ImageTk, ImageDraw, ImageFont

class StatsPage(ttk.Frame):
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
        label = Label(self.canvas, text="Input Stats Data", font=self.mainFont, bg='white', fg='#191D23')
        label.pack(pady=20, side=TOP, padx=0)
        # Create a window on the canvas and add the label to it
        self.canvas.create_window(200, 100, window=label, anchor=NW)
    
        # Attachment Section
        self.image = PhotoImage(file="./img/attacth_outerbox.png")
        image_id = self.canvas.create_image(170, 130, anchor=NW, image=self.image)
        image_id_x = 170
        image_id_width = self.image.width()
        # Cloud
        self.cloud = Image.open('./img/cloud.png').resize((55, 55))
        self.cloud = ImageTk.PhotoImage(self.cloud)
        cloud_width = self.cloud.width()
        cloud_height = self.cloud.height()
        # Cloud position
        cloud_x = image_id_x + (image_id_width - cloud_width) // 2
        cloud_id = self.canvas.create_image(cloud_x, 193, anchor=NW, image=self.cloud)
         # Text
        # Create a label with Manrope font
        sub_label = Label(self.canvas, text="Browse and chose the dataset you want to\n upload from your computer.\nStats files only.", font=self.subFont, bg='white', fg='#191D23')
        sub_label.pack(pady=20, padx=0)
        sub_width = sub_label.winfo_reqwidth()
        sub_textx = image_id_x + (image_id_width - sub_width) // 2
        self.canvas.create_window(sub_textx, 253, window=sub_label, anchor=NW)
        # Pack the canvas to make it visible
        self.canvas.pack(fill=BOTH, expand=YES)
        
        # Attach Btn as a button
        self.at_btn_command = lambda: self.attatch_file()  
        self.at_btn = Image.open('./img/attatch.png').resize((60, 60))
        self.at_btn = ImageTk.PhotoImage(self.at_btn)
        at_width = self.at_btn.width()
        at_btnx = image_id_x + (image_id_width - at_width) // 2
        self.at_btn_button = Button(self.canvas, image=self.at_btn, command=self.at_btn_command, borderwidth=0, highlightthickness=0)
        self.at_btn_button_window = self.canvas.create_window(at_btnx, 400, anchor=NW, window=self.at_btn_button)

    def attatch_file(self):
        # Open file dialog to choose a JSON file
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            print("Selected file:", file_path)
            # Perform actions with the selected file, e.g., read the JSON content
            with open(file_path, 'r') as file:
                json_content = file.read()
                print("JSON content:", json_content)

# You can include other methods or modify the existing ones based on your needs
