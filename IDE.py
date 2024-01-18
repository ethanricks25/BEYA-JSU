import tkinter as tk
from tkinter import filedialog, scrolledtext, ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import threading
import os

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Python IDE")
        self.root.geometry("1200x600")

        # Create a menu bar
        menubar = tk.Menu(root)
        root.config(menu=menubar)

        # Add file menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Create a PanedWindow for left and right panes
        paned_window = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
        paned_window.pack(fill=tk.BOTH, expand=True)

        # Left Pane, further divided into top and bottom
        left_pane = ttk.PanedWindow(paned_window, orient=tk.VERTICAL)
        paned_window.add(left_pane, weight=1)  # Add left pane to main paned window

        # Top Text Area in Left Pane
        self.top_text_area = scrolledtext.ScrolledText(left_pane, wrap=tk.WORD)
        left_pane.add(self.top_text_area, weight=1)  # Add top text area to left pane

        # Bottom Text Area in Left Pane
        self.bottom_text_area = scrolledtext.ScrolledText(left_pane, wrap=tk.WORD)
        left_pane.add(self.bottom_text_area, weight=1)  # Add bottom text area to left pane

        # Right Text Area
        self.right_text_area = scrolledtext.ScrolledText(paned_window, wrap=tk.WORD)
        paned_window.add(self.right_text_area, weight=2)  # Add right text area to main paned window

        # Add history and help menus
        history_menu = tk.Menu(menubar, tearoff=0)
        help_menu = tk.Menu(menubar, tearoff=0)

        menubar.add_cascade(label="History", menu=history_menu)
        menubar.add_cascade(label="Help", menu=help_menu)

        help_menu.add_command(label="About", command=self.show_help)
        self.file_history = []
        self.update_history_menu(history_menu)

        # Add plot menu
        plot_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Plot", menu=plot_menu)
        plot_menu.add_command(label="Plot Data", command=self.plot_data)


    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                self.top_text_area.delete(1.0, tk.END)
                self.top_text_area.insert(1.0, file.read())
        self.add_to_history(file_path)

    def save_file(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.top_text_area.get(1.0, tk.END))
    
    def add_to_history(self, file_path):
        if file_path not in self.file_history:
            self.file_history.append(file_path)
            self.update_history_menu()

    def update_history_menu(self, history_menu):
        history_menu.delete(0, tk.END)
        for file_path in self.file_history:
            history_menu.add_command(label=os.path.basename(file_path),
                                     command=lambda path=file_path: self.open_file_from_history(path))

    def open_file_from_history(self, file_path):
        with open(file_path, 'r') as file:
            self.top_text_area.delete(1.0, tk.END)
            self.top_text_area.insert(1.0, file.read())

    def plot_data(self):
        # Sample function to plot data
        data = self.top_text_area.get(1.0, tk.END)
        # ... code to handle data and plot ...

    def show_help(self):
        messagebox.showinfo("Help", "Information about how to use the application")

    def run_background_job(self, job_func):
        # Function to run a job in the background
        threading.Thread(target=job_func).start()

# Create the main window
root = tk.Tk()
editor = TextEditor(root)
root.mainloop()
