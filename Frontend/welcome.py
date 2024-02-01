from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont

class WelcomePage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.logo = ImageTk.PhotoImage(Image.open("./img/logos.png"))
        self.btn_image = None
        self.create_widgets()

    def create_widgets(self):
        self.canvas = Canvas(self, bg='white', highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=YES)

        self.image_on_canvas = self.canvas.create_image(0, 0, anchor=NW, image=self.logo)

        # Create rounded button image
        self.btn_image = self.create_rounded_button((150, 40), "Start", 20)

        # Use Label instead of Button to display the image
        btn_label = Label(self.canvas, image=self.btn_image, bd=0, bg='white')
        btn_label.bind("<Button-1>", self.on_button_click)  # Bind the click event

        # Calculate the x-coordinate to center the button horizontally
        canvas_width = self.canvas.winfo_width()
        btn_x = (canvas_width) // 2

        # Create window for the Label with the adjusted x-coordinate
        self.btn_canvas = self.canvas.create_window(btn_x, 0, window=btn_label, anchor="center")

        self.canvas.bind("<Configure>", self.resize_canvas)
        self.center_image()

    def create_rounded_button(self, image_size, text, radius):
        img = Image.new('RGBA', image_size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Draw a rounded rectangle
        draw.rounded_rectangle((0, 0, image_size[0], image_size[1]), radius, fill='#44546A')

        # Add text to the button using ImageFont module
        font = ImageFont.load_default()  # Use a default font
        text_bbox = draw.textbbox((0, 0), text, font=font)  # Corrected function name
        text_position = ((image_size[0] - text_bbox[2]) // 2, (image_size[1] - text_bbox[3]) // 2)
        draw.text(text_position, text, font=font, fill='white')

        # Convert the image to Tkinter format
        rounded_button_img = ImageTk.PhotoImage(img)

        return rounded_button_img

    def resize_canvas(self, event):
        canvas = event.widget
        canvas.config(width=event.width, height=event.height)
        self.center_image()

    def center_image(self):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        image_width = self.logo.width()
        btn_width = self.btn_image.width()
        image_height = self.logo.height()
        btn_height = self.btn_image.height()

        x = (canvas_width - image_width) // 2
        y_image = (canvas_height - image_height) // 2 - 80
        y_btn = (canvas_height + image_height) // 2 - 30  # Adjust the vertical distance between image and button
        x_btn = (canvas_width) // 2  # Adjust the vertical distance between image and button

        if self.master.winfo_toplevel().attributes('-fullscreen'):
            y_image = (canvas_height - image_height) // 2
            y_btn = (canvas_height + image_height) // 2 - 10  # Adjust the vertical distance between image and button

        self.canvas.coords(self.image_on_canvas, x, y_image)
        self.canvas.coords(self.btn_canvas, x_btn, y_btn)

    def on_button_click(self, event):
        # Switch to the InputDataPage
        self.master.master.notebook.select(1)  # Switch to the second page (index 1)
        self.master.master.notebook.tab(1, state='normal')  # Enable access to the second page
        self.master.master.notebook.tab(0, state='disabled')  # Enable access to the second page
