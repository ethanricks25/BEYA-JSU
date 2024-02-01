from tkinter import *
from tkinter import font,ttk,messagebox, filedialog
import tkinter as tk
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

    
    def create_widgets(self):
        window = tk.Tk()
       # window.geometry('900x900')
        #window.title('Tab Widget')

        # Create a frame on the left side
        left_frame = tk.Frame(window, width=400, height=400, bg='grey')
        left_frame.grid(row=4, column=4, padx=20, pady=20, sticky='nsw')

        # Create a frame in the bottom-left corner
        bottom_left_frame = tk.Frame(window, width=400, height=400, bg='grey')
        bottom_left_frame.grid(row=5, column=4, padx=20, pady=20, sticky='nsw')

        # Create a frame on the right side
        right_frame = tk.Frame(window, width=400, height=400, bg='grey')
        right_frame.grid(row=4, column=5, padx=20, pady=20, sticky='nsw')

    
