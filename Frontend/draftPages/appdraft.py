# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk, ImageDraw, ImageFont
# ##DRAFT DISREGAURD
# def resize_canvas(event):
#     canvas.config(width=event.width, height=event.height)
#     center_image()
#     below_image()

# def center_image():
#     canvas_width = canvas.winfo_width()
#     canvas_height = canvas.winfo_height()

#     image_width = logo.width()
#     image_height = logo.height()

#     x = (canvas_width - image_width) // 2
#     y = (canvas_height - image_height) // 2 - 100
#     if root.attributes('-fullscreen'):
#         # Center the image in full-screen mode
#         x = (canvas_width - image_width) // 2
#         y = (canvas_height - image_height) // 2
#     canvas.coords(image_on_canvas, x, y)

# def below_image():
#     canvas_width = canvas.winfo_width()
#     canvas_height = canvas.winfo_height()

#     x = (canvas_width) // 2
#     y = (canvas_height) // 2 + 110

#     canvas.coords(btn_canvas, x, y)

# def create_rounded_button(image_size, text, radius):
#     img = Image.new('RGBA', image_size, (0, 0, 0, 0))
#     draw = ImageDraw.Draw(img)

#     # Draw a rounded rectangle
#     draw.rounded_rectangle((0, 0, image_size[0], image_size[1]), radius, fill='#44546A')

#     # Add text to the button using ImageFont module
#     font = ImageFont.truetype("arial.ttf", 12)
#     text_bbox = draw.textbbox((0, 0), text, font=font)

#     # Calculate text position
#     text_position = ((image_size[0] - text_bbox[2]) // 2, (image_size[1] - text_bbox[3]) // 2)
#     draw.text(text_position, text, font=font, fill='white')

#     # Convert the image to Tkinter format
#     rounded_button_img = ImageTk.PhotoImage(img)

#     return rounded_button_img

# def on_button_click():
#     notebook.tab(1, state='normal')  # Enable access to the second page
#     notebook.tab(0, state='disabled')  # Enable access to the second page
#     notebook.select(1)  # Switch to the second page

# # Create object
# root = Tk()

# # Adjust size
# root.geometry("1000x800")
# root.configure(background='white')
# root.minsize(1000, 800)

# # giving title to the main window
# root.title("PRISM")
# p1 = PhotoImage(file='./img/p.png')
# root.iconphoto(False, p1)

# # Create a notebook (tabbed layout)
# notebook = ttk.Notebook(root)

# ## Welcome Page ##
# # Create a canvas with no border for the first page
# canvas = Canvas(notebook, bg='white', highlightthickness=0)
# canvas.pack(fill=BOTH, expand=YES)

# # Load an image in the script
# logo = ImageTk.PhotoImage(Image.open("./img/prismlogo.png"))

# # components
# image_on_canvas = canvas.create_image(0, 0, anchor=NW, image=logo)

# # Create a rounded button image
# btn_image = create_rounded_button((150, 40), "Start", 20)

# # Create a transparent canvas item for the button
# btn = Button(canvas, image=btn_image, bd=0, command=on_button_click, bg='white')
# btn_canvas = canvas.create_window(0, 0, window=btn, anchor="center")





# ##Notebook navigation
# # Add the first page to the notebook
# notebook.add(canvas, text='Welcome')

# # Create a canvas with no border for the second page
# canvas2 = Canvas(notebook, bg='white', highlightthickness=0)


# ##Page 2
# # Add the second page to the notebook with state='disabled'
# notebook.add(canvas2, text='Input Data', state='disabled')

# btn = Button(canvas2,text='TBD' , bg='white')
# btn_canvas2 = canvas2.create_window(100, 100, window=btn, anchor="center")


# # Bind the resize_canvas function to the window resize event
# root.bind("<Configure>", resize_canvas)

# # Center the image initially
# center_image()

# # Execute tkinter
# notebook.pack(fill=BOTH, expand=YES)
# root.mainloop()
