import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import subprocess
import threading
import sys

window = tk.Tk()
window.geometry('900x900')
window.title('Tab Widget')

# Create a frame on the left side
left_frame = tk.Frame(window, width=400, height=400, bg='grey')
left_frame.grid(row=4, column=4, padx=20, pady=20, sticky='nsw')

# Create a terminal in the left frame
terminal = scrolledtext.ScrolledText(left_frame, wrap=tk.WORD)
terminal.pack(expand=True, fill='both')  # Make the terminal fill the left_frame

# Terminal Prompt
terminal_prompt = ">>> "
terminal.insert(tk.END, terminal_prompt)

def execute_command(event):
    """ Execute the command entered in the terminal. """
    full_command = terminal.get("end-2l linestart", "end-1c")
    command = full_command.strip()
    
    if command.startswith(terminal_prompt):
        command = command[len(terminal_prompt):]  # Remove the prompt from command

    terminal.insert(tk.END, '\n')  # Move to next line after command
    
    if command:  # Check if command is not empty
        if command.startswith("!"):  # Prefix for shell commands
            command = command[1:]  # Remove '!' from command
            run_shell_command(command)
        else:
            run_python_command(command)

    terminal.insert(tk.END, terminal_prompt)  # Add prompt for next command
    return 'break'  # prevent the default return key behavior

def run_python_command(command):
    """ Run a Python command. """
    try:
        exec(command, globals(), locals())
    except Exception as e:
        terminal.insert(tk.END, f'Error: {e}\n')

def run_shell_command(command):
    """ Run a shell command in a separate thread. """
    def run():
        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output = result.stdout
        except subprocess.CalledProcessError as e:
            output = f'Error: {e}\n{e.stderr}'
        terminal.insert(tk.END, output + terminal_prompt)
    threading.Thread(target=run).start()

# Bind the Return key to execute_command function
terminal.bind('<Return>', execute_command)

# Create a frame in the bottom-left corner
bottom_left_frame = tk.Frame(window, width=400, height=400, bg='grey')
bottom_left_frame.grid(row=5, column=4, padx=20, pady=20, sticky='nsw')

# Create a frame on the right side
right_frame = tk.Frame(window, width=400, height=400, bg='grey')
right_frame.grid(row=4, column=5, padx=20, pady=20, sticky='nsw')

window.mainloop()