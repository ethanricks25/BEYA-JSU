import tkinter as tk
from tkinter import Listbox, END, Entry, Scrollbar
import subprocess
#Hannah page below

class LeftFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        self.input_entry = Entry(self)
        self.input_entry.pack()

        
        self.listbox = Listbox(self, height=10, width=50)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        scrollbar = Scrollbar(self, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox.config(yscrollcommand=scrollbar.set)

        run_button = tk.Button(self, text="Run Script", command=self.run_script)
        run_button.pack()

    def run_script(self):
        try:
            user_input = self.input_entry.get()
            command = ["python", "script.py", user_input]
            output = subprocess.check_output(command, text=True, stderr=subprocess.STDOUT)
            self.listbox.insert(END, output)
        except subprocess.CalledProcessError as e:
            self.listbox.insert(END, f'Error: {e.output}')

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Tkinter App")
        #self.geometry('900x900')

        self.grid_columnconfigure(0, weight=1)  
        self.grid_columnconfigure(1, weight=1)  
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        
        left_frame = LeftFrame(self)
        left_frame.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

        bottom_right_frame = tk.Frame(self, width=400, height=400, bg='grey')
        bottom_right_frame.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')

    
        top_right_frame = tk.Frame(self, width=400, height=400, bg='grey')
        top_right_frame.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')

# if __name__ == "__main__":
#     app = App()
#     app.mainloop()