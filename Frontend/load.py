from tkinter import *
from tkinter import font, ttk, messagebox, filedialog
from PIL import Image, ImageTk, ImageSequence  # Import ImageSequence

class LoadData(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.logo = Image.open('./img/logonw.png').resize((600, 260))
        self.logo = ImageTk.PhotoImage(self.logo)
        self.gif1 = Image.open('./img/pbg.gif')
        self.gif2 = Image.open('./img/sp.gif')  # Path to your second GIF
        self.gif_frames1 = [ImageTk.PhotoImage(self.gif_frame) for self.gif_frame in ImageSequence.Iterator(self.gif1)]
        self.gif_frames2 = [ImageTk.PhotoImage(self.gif_frame) for self.gif_frame in ImageSequence.Iterator(self.gif2)]
        self.image_on_canvas = None  # Initialize image object
        self.gif_label1 = None
        self.gif_label2 = None
        self.timer_running = False  # Flag to track whether the timer is running
        self.create_widgets()
        self.animate_gif(0, self.gif_frames1, 0.7, self.gif_label1)  # Adjust the position and speed for the first GIF
        self.animate_gif(0, self.gif_frames2, 0.8, self.gif_label2)  # Adjust the position and speed for the second GIF

    def create_widgets(self):
        self.canvas = Canvas(self, bg='white', highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=YES)

        # Bind the canvas to handle resize
        self.canvas.bind("<Configure>", self.resize_canvas)

        # Create the image on the canvas
        canvas_width = self.canvas.winfo_width()
        logo_width = self.logo.width()
        imgx = (canvas_width - logo_width) // 2
        imgy = (self.canvas.winfo_height() - self.logo.height()) // 2
        self.image_on_canvas = self.canvas.create_image(imgx, imgy, anchor=NW, image=self.logo)

        # Create Label widgets for the GIFs
        self.gif_index1 = 0
        self.gif_label1 = Label(self.canvas, image=self.gif_frames1[self.gif_index1], bg='white')
        self.gif_label1.image = self.gif_frames1[self.gif_index1]  # To prevent garbage collection
        self.gif_label1.place(relx=0.5, rely=0.8, anchor='center')

        self.gif_index2 = 0
        self.gif_label2 = Label(self.canvas, image=self.gif_frames2[self.gif_index2], bg='white')
        self.gif_label2.image = self.gif_frames2[self.gif_index2]  # To prevent garbage collection
        self.gif_label2.place(relx=0.5, rely=0.22, anchor='center')

        # Periodically check the condition for starting the timer and switching to the next page
        self.check_condition()

    def resize_canvas(self, event):
        # Handle canvas resize and center the image
        canvas_width = event.width
        logo_width = self.logo.width()
        imgx = (canvas_width - logo_width) // 2
        imgy = (self.canvas.winfo_height() - self.logo.height()) // 2
        self.canvas.coords(self.image_on_canvas, imgx, imgy)

    def check_condition(self):
        # Check the condition for starting the timer and switching to the next page
        if (
            self.master.master.notebook.index(self.master.master.notebook.select()) == 3
            and not self.timer_running
        ):
            self.start_timer()
            return
        # Continue checking periodically
        self.after(100, self.check_condition)

    def switch_to_input_page(self):
        # Switch to the InputDataPage
        self.master.master.notebook.tab(4, state='normal')  # Enable access to the fifth page
        self.master.master.notebook.tab(3, state='disabled')  # Disable access to the fourth page
        self.master.master.notebook.select(4)  # Switch to the fifth page (index 4)
        print("SWITCH!")

    def animate_gif(self, index, frames, speed, label):
        gif_index = (index + 1) % len(frames)
        label.configure(image=frames[gif_index])
        label.image = frames[gif_index]  # To prevent garbage collection
        self.after(int(100 / speed), lambda: self.animate_gif(gif_index, frames, speed, label))

    def start_timer(self):
        # Start the timer
        self.timer_running = True
        self.after(8000, self.switch_to_input_page)

