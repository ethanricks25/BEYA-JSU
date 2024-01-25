# main.py
from tkinter import *
from tkinter import ttk
from welcome import WelcomePage
from inputStats import InputDataPage
from stats import StatsPage
from load import LoadData
from fresults import Results

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("PRISM")
        self.geometry("1000x700")
        self.configure(background='white')
        self.minsize(1000, 700)

        # Create a Notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=BOTH, expand=YES)
        #giving title to the main window
        self.title("PRISM")
        p1 = PhotoImage(file='./img/sm.png')
        self.iconphoto(False, p1)
        # Create welcome page
        welcome_page = WelcomePage(self.notebook)
        welcome_page.pack(fill=BOTH, expand=YES)
        self.notebook.add(welcome_page, text="Welcome")

        # Create input data page
        input_data_page = InputDataPage(self.notebook)
        input_data_page.pack(fill=BOTH, expand=YES)
        self.notebook.add(input_data_page, text="Input Data",state='disabled')
        # Create Stats Page
        stats_page = StatsPage(self.notebook)
        stats_page.pack(fill=BOTH, expand=YES)
        self.notebook.add(stats_page, text="Input Stats",state='disabled')    
        
        # Create SplashLoad Page
        load_page = LoadData(self.notebook)
        load_page.pack(fill=BOTH, expand=YES)
        self.notebook.add(load_page, text="Loading",state='disabled')  
          
        # Create Results Page
        r_page = Results(self.notebook)
        r_page.pack(fill=BOTH, expand=YES)
        self.notebook.add(r_page, text="Results",state='disabled')    
                               
        self.mainloop()

if __name__ == "__main__":
    app = MainApp()
