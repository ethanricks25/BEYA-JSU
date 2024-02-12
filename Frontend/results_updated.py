import tkinter as tk
from tkinter import END
from tkinter import *
from tkinter import ttk, scrolledtext
from tkintermapview import TkinterMapView  # Import TkinterMapView
import pandas as pd
import find_hospitals
import subprocess
import threading
import sys
class StdoutRedirector(object):
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END)  # Scroll to the bottom

    def flush(self):
        pass  # This might be called by some print statements, so it's safe to include it.

class ResultsFrame(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.master = master
        self.inputStats_df = None
        self.stats_df = None
        self.create_widgets()
        self.original_stdout = sys.stdout  # Keep track of the original stdout, so you can restore it later
        self.original_stderr = sys.stderr  # Keep track of the original stderr

        self.stdout_redirector = StdoutRedirector(self.terminal)
        sys.stdout = self.stdout_redirector
        sys.stderr = self.stdout_redirector



class StdoutRedirector(object):
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert(tk.END, string)
        self.text_widget.see(tk.END)  # Scroll to the bottom

    def flush(self):
        pass  # This might be called by some print statements, so it's safe to include it.

class ResultsFrame(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.master = master
        self.inputStats_df = None
        self.stats_df = None
        self.create_widgets()
        self.original_stdout = sys.stdout  # Keep track of the original stdout, so you can restore it later
        self.original_stderr = sys.stderr  # Keep track of the original stderr

        self.stdout_redirector = StdoutRedirector(self.terminal)
        sys.stdout = self.stdout_redirector
        sys.stderr = self.stdout_redirector

    def create_widgets(self):
        style = ttk.Style()
        style.configure('My.TFrame', background='white', borderwidth=2, relief='solid')

        # Create a container frame to center everything
        container_frame = ttk.Frame(self)
        container_frame.pack(expand=YES, fill=BOTH, anchor=CENTER, padx=50, pady=50)

        # Create a notebook widget
        notebook = ttk.Notebook(container_frame)
        notebook.pack(expand=YES, fill=BOTH)

        # Create the first tab
        tab1 = ttk.Frame(notebook)
        notebook.add(tab1, text="Notes")

        # Create the first column with two frames inside tab1
        column1_frame = ttk.Frame(tab1)
        column1_frame.pack(side=LEFT, padx=(0, 10), expand=YES, fill=BOTH)

        frame1 = ttk.Frame(column1_frame, style='My.TFrame')
        frame1.pack(side=TOP, pady=(0, 10), expand=YES, fill=BOTH)
        # Set fixed dimensions for frame1
        frame1.grid_propagate(False)
        frame1.grid_rowconfigure(0, weight=1)
        frame1.grid_columnconfigure(0, weight=1)
        frame1['width'] = 300  # Adjust the width as needed
        frame1['height'] = 280  # Adjust the height as needed

        # Simple terminal (Text widget)
        terminal = Text(frame1, wrap=WORD, height=10, width=30)  # Adjust width here
        terminal.pack(expand=YES, fill=BOTH)

        frame2 = ttk.Frame(column1_frame, style='My.TFrame')
        frame2.pack(side=TOP, pady=(0, 10), expand=YES, fill=BOTH)
        # Set fixed dimensions for frame2
        frame2.grid_propagate(False)
        frame2.grid_rowconfigure(0, weight=1)
        frame2.grid_columnconfigure(0, weight=1)
        frame2['width'] = 300  # Adjust the width as needed
        frame2['height'] = 280  # Adjust the height as needed

        # Create the second column with one frame inside tab1
        column2_frame = ttk.Frame(tab1)
        column2_frame.pack(side=LEFT, expand=YES, fill=BOTH)

        frame3 = ttk.Frame(column2_frame, style='My.TFrame')
        frame3.pack(side=TOP, expand=YES, fill=BOTH)
        # Set fixed dimensions for frame3
        frame3.grid_propagate(False)
        frame3.grid_rowconfigure(0, weight=1)
        frame3.grid_columnconfigure(0, weight=1)
        frame3['width'] = 500  # Adjust the width as needed
        frame3['height'] = 600  # Adjust the height as needed

        # Add TkinterMapView to frame3
        self.map_view = TkinterMapView(frame3)
        self.map_view.pack(expand=YES, fill=BOTH)

        # Add terminal setup here
        self.terminal = scrolledtext.ScrolledText(frame1, wrap="word", height=10, width=30)  # Adjust width here
        self.terminal.pack(expand=True, fill="both")
        self.terminal_prompt = ">>> "
        self.terminal.insert("end", self.terminal_prompt)

        # Bind the Return key to execute_command function
        self.terminal.bind('<Return>', self.execute_command)

    def execute_command(self, event):
        full_command = self.terminal.get("end-2l linestart", "end-1c")
        command = full_command.strip()[len(self.terminal_prompt):]

        self.terminal.insert("end", '\n')  # Move to next line after command

        if command.startswith("!"):
            self.run_shell_command(command[1:])  # Shell command
        else:
            self.run_python_command(command)  # Python command

        self.terminal.insert("end", self.terminal_prompt)  # Add prompt for next command
        return 'break'  # Prevent default 'Return' key behavior

    def run_python_command(self, command):
        # Ensure the command is correctly formatted
        command = command.strip()
        if not command:
            return  # Avoid executing empty commands
        
        # Execute the command within a defined global context
        try:
            exec(command, globals(), locals())
        except Exception as e:
            self.terminal.insert("end", f'Error: {e}\n')

    def run_shell_command(self, command):
        def run():
            try:
                result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                output = result.stdout
            except subprocess.CalledProcessError as e:
                output = f'Error: {e}\n{e.stderr}'
            self.terminal.insert("end", output + self.terminal_prompt)
        threading.Thread(target=run).start()

    def set_dfs(self, df1, df2):
        self.inputStats_df = df1
        self.stats_df = df2
        print("Set dataframes for results page!")
        return

    def analyze_patients_csv(self):
        race_counts = self.inputStats_df['RACE'].value_counts() #pandas series
        race_counts.drop('other', inplace=True)
        total_population: int = sum(race_counts.values)
        race_percentages: dict[str, float] = { race : race_count / total_population for race, race_count in race_counts.items()}
        return race_percentages
        
    
    def analyze_census_csv(self):
        population_data = self.stats_df 
        # Don't want to change dataset stored by class
        population_data.iloc[ : , 1] = population_data.iloc[ : , 1].str.replace(",", "").astype(int)
        # Convert Column 1 data to integers

        total_population: int = population_data.iloc[0, 1]
        caucasian : int = int(population_data.iloc[2, 1]) + population_data.iloc[10:16 , 1].sum()
        african_american : int = int(population_data.iloc[3, 1]) + population_data.iloc[16:20 , 1].sum()
        native : int = int(population_data.iloc[4, 1]) + population_data.iloc[20:23 , 1].sum()
        asian : int = int(population_data.iloc[5, 1]) + population_data.iloc[23:25 , 1].sum()
        pacific_islander : int = int(population_data.iloc[6, 1]) + population_data.iloc[25 , 1]
        other : int = int(population_data.iloc[7, 1])
        print(caucasian, african_american, native, asian, pacific_islander, other)
        # Count different races

        race_counts = pd.Series({
        "white" : caucasian,
        "black" : african_american,
        "native" : native,
        "asian" : asian,
        "pacific islander" : pacific_islander, 
        "other": other
        }) 
        race_counts.drop("other", inplace=True)

        race_percentages: dict[str, float] = { race : race_count / total_population for race, race_count in race_counts.items()}

        print("Analyzation of target populations complete!")
        return race_percentages

    def compare_patients_to_census(self, patient_data : dict[str, float], census_data : dict[str, float]):
        disparity_dict : dict[str, float] = { race : abs( race_count_patients - census_data[race]) for race, race_count_patients in patient_data.items() }
        underrepresented_race: str = min(disparity_dict, key=lambda k: disparity_dict[k])
        print("Comparison of datasets complete!")
        print("The underrepresented population is: ")
        print(underrepresented_race)
        return ( disparity_dict, underrepresented_race, disparity_dict[underrepresented_race] )
    
    def update_map(self, hospital_data):
        for name, lat, lng in zip(hospital_data.iloc[:]["name"], hospital_data.iloc[:]["lat"], hospital_data.iloc[:]["lng"]):
            self.map_view.set_marker(lat, lng, text=name)
        bottom_right = (min(hospital_data.iloc[:]["lat"]) - .15, max(hospital_data.iloc[:]["lng"]) + .15)
        top_left = (max(hospital_data.iloc[:]["lat"]) + .15, min(hospital_data.iloc[:]["lng"]) - .15)
        self.map_view.fit_bounding_box( top_left , bottom_right )
        
    def __del__(self):
        sys.stdout = self.original_stdout
        sys.stderr = self.original_stderr
