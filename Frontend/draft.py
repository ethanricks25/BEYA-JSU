from tkinter import *
from PIL import Image, ImageTk

def resize_canvas(event):
    canvas.config(width=event.width, height=event.height)
    center_image()

def center_image():
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    image_width = logo.width()
    image_height = logo.height()

    x = (canvas_width - image_width) // 2
    y = (canvas_height - image_height) // 2

    canvas.coords(image_on_canvas, x, y)

# Create object
root = Tk()

# Adjust size
root.geometry("1000x600")
root.configure(background='white')
root.minsize(1000, 600)

# giving title to the main window
root.title("PRISM")
p1 = PhotoImage(file='./img/p.png')
root.iconphoto(False, p1)

# Create a frame to hold the grid layout
frame = Frame(root, bg='white')
frame.pack(fill=BOTH, expand=YES)

# Create a canvas with no border and add it to the frame
canvas = Canvas(frame, bg='white', highlightthickness=0)
# Load an image in the script
logo = ImageTk.PhotoImage(Image.open("./img/prismlogo.png"))
# Add image to the Canvas Items and get its id
image_on_canvas = canvas.create_image(0, 0, anchor=NW, image=logo)
# Create a button and add it to the frame, placing it in the second row (row=1)
button = Button(frame, text="Click me!")


# define grid
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
# frame.rowconfigure(2, weight=1)


#Place Widgets
canvas.grid(row=0, column=0, sticky="nsew",pady=0)
button.grid(row=1,column=0,sticky='n',ipadx  = 43,ipady=12)

# Bind the resize_canvas function to the window resize event
root.bind("<Configure>", resize_canvas)

# Center the image initially
center_image()

# Execute tkinter
root.mainloop()
