from tkinter import *
from tkinter import font,ttk,messagebox, filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont
import pandas as pd

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
        sub_label = Label(self.canvas, text="Browse and chose the dataset you want to\n upload from your computer.\n CSV files only.", font=self.subFont, bg='white', fg='#191D23')
        sub_label.pack(pady=20, padx=0)
        sub_width = sub_label.winfo_reqwidth()
        sub_textx = image_id_x + (image_id_width - sub_width) // 2
        self.canvas.create_window(sub_textx, 253, window=sub_label, anchor=NW)
        # Pack the canvas to make it visible
        self.canvas.pack(fill=BOTH, expand=YES)
        
        # Attach Btn as a button
        self.at_btn_command = lambda: self.attach_file()  
        self.at_btn = Image.open('./img/attatch.png').resize((60, 60))
        self.at_btn = ImageTk.PhotoImage(self.at_btn)
        at_width = self.at_btn.width()
        at_btnx = image_id_x + (image_id_width - at_width) // 2
        self.at_btn_button = Button(self.canvas, image=self.at_btn, command=self.at_btn_command, borderwidth=0, highlightthickness=0)
        self.at_btn_button_window = self.canvas.create_window(at_btnx, 400, anchor=NW, window=self.at_btn_button)

    def attach_file(self):
        # Open file dialog to choose a CSV file
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            print("Selected file:", file_path)
            # Check if the file has the correct extension
            if file_path.lower().endswith('.csv'):
                # Perform actions with the selected file, e.g., read the CSV content
                df = pd.read_csv(file_path)
                print("CSV content:", df)
            else:
                # Notify user about the wrong file type
                messagebox.showerror("Wrong File Type", "Please choose a CSV file.")
            self.master.master.notebook.tab(3, state='normal')  # Enable access to the third page
            self.master.master.notebook.tab(2, state='disabled')  # Enable access to the second page
            self.master.master.notebook.tab(1, state='disabled')  # Enable access to the second page
            self.master.master.notebook.tab(0, state='disabled')  # Enable access to the second page
            self.master.master.notebook.select(3)  # Switch to the second page (index 1)
        else:
            # Notify user about not selecting any file
            messagebox.showinfo("No File Selected", "You did not select any file.")

# You can include other methods or modify the existing ones based on your needs
