# welcome_page.py
from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
from input import InputDataPage  # Import the InputDataPage class
##DRAFT DISREGAURD
##DRAFT DISREGAURD

class WelcomePage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.logo = ImageTk.PhotoImage(Image.open("./img/prismlogo.png"))
        self.image_on_canvas = None
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

        # Create window for the Label
        self.btn_canvas = self.canvas.create_window(0, 0, window=btn_label, anchor="center")

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
        image_height = self.logo.height()

        x = (canvas_width - image_width) // 2
        y = (canvas_height - image_height) // 2 - 100
        if self.master.attributes('-fullscreen'):
            x = (canvas_width - image_width) // 2
            y = (canvas_height - image_height) // 2
        self.canvas.coords(self.image_on_canvas, x, y)

    def on_button_click(self, event):
        # Switch to the InputDataPage
        self.destroy()  # Destroy the current page
        input_data_page = InputDataPage(self.master)
        input_data_page.pack(fill=BOTH, expand=YES)  # Show the InputDataPage

if __name__ == "__main__":
    root = Tk()

    # Set the initial size
    root.geometry("1000x800")
    root.configure(background='white')
    root.minsize(1000, 800)

    # Create welcome page
    welcome_page = WelcomePage(root)
    welcome_page.pack(fill=BOTH, expand=YES)

    root.mainloop()
