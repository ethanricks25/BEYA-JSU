from tkinter import *
from tkinter import ttk
from welcome import WelcomePage
from hospDs import HospPage
from modelDs import ModelPage
from load import LoadData
from fresults import Results
# from ide import TextEditor
# Import the LeftFrame class
from results_updated import ResultsFrame  # Replace 'your_module_name' with the actual module name
import find_hospitals

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

        # Create hospDS  page
        self.input_data_page = HospPage(self.notebook)
        self.input_data_page.pack(fill=BOTH, expand=YES)
        self.notebook.add(self.input_data_page, text="Hospital Dataset ", state='disabled')

        # Create modelDs Page
        self.stats_page = ModelPage(self.notebook)
        self.stats_page.pack(fill=BOTH, expand=YES)
        self.notebook.add(self.stats_page, text="Model Training Dataset", state='disabled')    
        
        # Create SplashLoad Page
        load_page = LoadData(self.notebook)
        load_page.pack(fill=BOTH, expand=YES)
        self.notebook.add(load_page, text="Loading", state='disabled')  
          
        # # Create Results Page
        # r_page = Results(self.notebook)
        # r_page.pack(fill=BOTH, expand=YES)
        # self.notebook.add(r_page, text="Results", state='normal')    

        #Hannah page below
        # Create LeftFrame as a notebook page
        self.results_frame = ResultsFrame(self.notebook)
        self.results_frame.pack(fill=BOTH, expand=YES)
        self.notebook.add(self.results_frame, text="Results", state='normal')  # Adjust the state as needed

        self.notebook.bind("<<NotebookTabChanged>>", self.handle_tab_change)
        # # Create TextEditor as a notebook page
        # text_editor_frame = TextEditor(self.notebook)
        # text_editor_frame.pack(fill=BOTH, expand=YES)
        # self.notebook.add(text_editor_frame, text="Text Editor", state='normal')  # Adjust the state as needed
        self.mainloop()
    
    def handle_tab_change(self, event):
        selected_tab_index = self.notebook.index('current')

        if selected_tab_index == 3:
            self.results_frame.set_dfs(self.input_data_page.get_df(), self.stats_page.get_df())
            disparities, race_of_interest, disparity_of_roi = self.results_frame.compare_patients_to_census(self.results_frame.analyze_patients_csv(),self.results_frame.analyze_census_csv())
            hospital_object = find_hospitals.finding_hospitals(race_of_interest, "TX")
            hospitals = hospital_object.get_hospitals()
            print(hospitals.iloc[:]["name"])
            hospitals.iloc[:]["lat"] = hospitals.iloc[:]["lat"].astype(float)
            hospitals.iloc[:]["lng"] = hospitals.iloc[:]["lng"].astype(float)
            self.results_frame.update_map(hospitals)
        
if __name__ == "__main__":
    app = MainApp()
