from tkinter import *
from tkinter import ttk

class ResultsFrame(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure('My.TFrame', background='white', borderwidth=2, relief='solid')
        # Create a container frame to center everything
        container_frame = ttk.Frame(self)
        container_frame.pack(expand=YES, fill=BOTH, anchor=CENTER, padx=50, pady=50)

        # Create the first column with two frames
        column1_frame = ttk.Frame(container_frame)
        column1_frame.pack(side=LEFT, padx=(0, 10), expand=YES, fill=BOTH)

        frame1 = ttk.Frame(column1_frame, style='My.TFrame')
        frame1.pack(side=TOP, pady=(0, 10), expand=YES, fill=BOTH)

        frame2 = ttk.Frame(column1_frame, style='My.TFrame')
        frame2.pack(side=TOP, pady=(0, 10), expand=YES, fill=BOTH)

        # Create the second column with one frame
        column2_frame = ttk.Frame(container_frame)
        column2_frame.pack(side=LEFT, expand=YES, fill=BOTH)

        frame3 = ttk.Frame(column2_frame, style='My.TFrame')
        frame3.pack(side=TOP, expand=YES, fill=BOTH)

# Rest of your code...
