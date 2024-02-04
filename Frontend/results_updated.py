from tkinter import *
from tkinter import ttk
import webbrowser
import folium

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
        # Set fixed dimensions for frame1
        frame1.grid_propagate(False)
        frame1.grid_rowconfigure(0, weight=1)
        frame1.grid_columnconfigure(0, weight=1)
        frame1['width'] = 300  # Adjust the width as needed
        frame1['height'] = 200  # Adjust the height as needed

        # Simple terminal (Text widget)
        terminal = Text(frame1, wrap=WORD, height=10, width=30)
        terminal.pack(expand=YES, fill=BOTH)

        frame2 = ttk.Frame(column1_frame, style='My.TFrame')
        frame2.pack(side=TOP, pady=(0, 10), expand=YES, fill=BOTH)
        # Set fixed dimensions for frame2
        frame2.grid_propagate(False)
        frame2.grid_rowconfigure(0, weight=1)
        frame2.grid_columnconfigure(0, weight=1)
        frame2['width'] = 300  # Adjust the width as needed
        frame2['height'] = 200  # Adjust the height as needed

        # Create the second column with one frame
        column2_frame = ttk.Frame(container_frame)
        column2_frame.pack(side=LEFT, expand=YES, fill=BOTH)

        frame3 = ttk.Frame(column2_frame, style='My.TFrame')
        frame3.pack(side=TOP, expand=YES, fill=BOTH)
        # Set fixed dimensions for frame3
        frame3.grid_propagate(False)
        frame3.grid_rowconfigure(0, weight=1)
        frame3.grid_columnconfigure(0, weight=1)
        frame3['width'] = 500  # Adjust the width as needed
        frame3['height'] = 600  # Adjust the height as needed

        # Display the Folium map using a WebView
        map_view = WebViewWidget(frame3, html_file_path="map.html")
        map_view.pack(expand=YES, fill=BOTH)

class WebViewWidget(Frame):
    def __init__(self, parent, html_file_path):
        Frame.__init__(self, parent)
        self.html_file_path = html_file_path
        self.create_widgets()

    def create_widgets(self):
        open_button = Button(self, text="Open Map in Browser", command=self.open_map)
        open_button.pack(side=TOP, pady=10)

    def open_map(self):
        webbrowser.open(self.html_file_path)

