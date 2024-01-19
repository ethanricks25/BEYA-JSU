# input_data_page.py
from tkinter import *

class InputDataPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        canvas = Canvas(self, bg='white', highlightthickness=0)
        canvas.pack(fill=BOTH, expand=YES)

        btn = Button(canvas, text='TBD', bg='white')
        btn_canvas = canvas.create_window(100, 100, window=btn, anchor="center")

# Execute only when run as a script
if __name__ == "__main__":
    root = Tk()
    input_data_page = InputDataPage(root)
    input_data_page.pack(fill=BOTH, expand=YES)
    root.mainloop()
