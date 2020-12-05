"""The NBA Project - GUI is the last portion of the project and currently in working progress"""

import tkinter as tk
import nba_project as np
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk 
#FigureCanvasTkAgg

class Window(tk.Frame):
    
    def __init__(self, master = None):
        tk.Frame.__init__(self)
        
        self.master = master    #Defines this as the main window(frame)
        self.main_window()
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.master.title("NBA stats")
        self.pack(fill='both' ,expand=1)
        
    
        def display_page(self,cont):
            frame = self.frames[cont]
            frame.tkraise()
        
    
class HomePage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        #Creates a label for the home page
        label=tk.Label(self,text="Home")
        #Puts the label for the home page in the window
        label.pack(pady=10,padx=10)
        
        #Cretes a home button
        home_button = tk.Button(self,text="Home",command=controller.display_page(HomePage))
        #Places the home button in the window
        home_button.pack()
        
        #Creates a GameRecap button
        game_recap_button = tk.Button(self,text="Game Recap",command=controller.display_page(GameRecap))
        #Places the button in the window
        game_recap_button.pack()
        
        #Cretes a rebound stats button
        rebound_stats_button = tk.Button(self,text="Rebound stats",command=controller.display_page(ReboundStats))
        #Places the rebound stats button in the window
        rebound_stats_button.pack()
        
        #Cretes a scoring stats button
        scoring_stats_button = tk.Button(self,text="Scoring stats",command=controller.display_page(HomePage))
        #Places the scoring stats button in the window
        scoring_stats_button.pack()
        
        assists_stats_button = tk.Button(self,text="Assists stats",command= controller.display_page(AssistStats))
        #Places the assists stats button in the window
        assists_stats_button.pack()
        
        
class GameRecap(tk.Frame):
    """Shows the points socred per quarter by each team.
    
    Args:
        tk.Frame: The frame(window) to display information. 
    """
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,controller)
        label = tk.Label(self,text="Points per team during the game")
        label.pack(pdy=10,padx=10)
        
        #Figure is the graph object itself thats passed in as the first arg
        canvas = tk.FigureCanvasTkAgg(figure,self)
        canvas.show()
        canvas.get_tk_widget().pack()
        
        #Creates the toolbar for the graph
        toolbar = tk.NavigationToolBar2Tk(canvas,self)
        toolbar.update()
        
        #Places the toolbar in the window
        canvas.get_tk_widget().pack()
        
        
        #Cretes a home button
        home_button = tk.Button(self,text="Home",command=controller.display_page(HomePage))
        #Places the home button in the window
        home_button.pack()
        
        #Creates a GameRecap button
        game_recap_button = tk.Button(self,text="Game Recap",command=controller.display_page(GameRecap))
        #Places the button in the window
        game_recap_button.pack()
        
        #Cretes a rebound stats button
        rebound_stats_button = tk.Button(self,text="Rebound stats",command=controller.display_page(ReboundStats))
        #Places the rebound stats button in the window
        rebound_stats_button.pack()
        
        #Cretes a scoring stats button
        scoring_stats_button = tk.Button(self,text="Scoring stats",command=controller.display_page(ScoringStats))
        #Places the scoring stats button in the window
        scoring_stats_button.pack()
        
        assists_stats_button = tk.Button(self,text="Assists stats",command= controller.display_page(AssistStats))
        #Places the assists stats button in the window
        assists_stats_button.pack()        
        
        
class ScoringStats(tk.Frame):
    """Shows the points socred per quarter by each team.
    
    Args:
        tk.Frame: The frame(window) to display information. 
    """
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,controller)
        label = tk.Label(self,text="Points per team during the game")
        label.pack(pdy=10,padx=10)
        
        #Figure is the graph object itself thats passed in as the first arg
        canvas = tk.FigureCanvasTkAgg(np.nba_gamestats.nbagame_summaryscore,self)
        canvas.show()
        canvas.get_tk_widget().pack()
        
        #Creates the toolbar for the graph
        toolbar = tk.NavigationToolBar2Tk(canvas,self)
        toolbar.update()
        
        #Places the toolbar in the window
        canvas.get_tk_widget().pack()
        
        
        #Cretes a home button
        home_button = tk.Button(self,text="Home",command=controller.display_page(HomePage))
        #Places the home button in the window
        home_button.pack()
        
        #Creates a GameRecap button
        game_recap_button = tk.Button(self,text="Game Recap",command=controller.display_page(GameRecap))
        #Places the button in the window
        game_recap_button.pack()
        
        #Cretes a rebound stats button
        rebound_stats_button = tk.Button(self,text="Rebound stats",command=controller.display_page(ReboundStats))
        #Places the rebound stats button in the window
        rebound_stats_button.pack()
        
        #Cretes a scoring stats button
        scoring_stats_button = tk.Button(self,text="Scoring stats",command=controller.display_page(ScoringStats))
        #Places the scoring stats button in the window
        scoring_stats_button.pack()
        
        assists_stats_button = tk.Button(self,text="Assist stats",command= controller.display_page(AssistStats))
        #Places the assists stats button in the window
        assists_stats_button.pack()
        
class ReboundStats(tk.Frame):
    """Shows the points socred per quarter by each team.
    
    Args:
        tk.Frame: The frame(window) to display information. 
    """
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,controller)
        label = tk.Label(self,text="Points per team during the game")
        label.pack(pdy=10,padx=10)
        
        #Figure is the graph object itself thats passed in as the first arg
        canvas = tk.FigureCanvasTkAgg(figure,self)
        canvas.show()
        canvas.get_tk_widget().pack()
        
        #Creates the toolbar for the graph
        toolbar = tk.NavigationToolBar2Tk(canvas,self)
        toolbar.update()
        
        #Places the toolbar in the window
        canvas.get_tk_widget().pack()
        
        
        #Cretes a home button
        home_button = tk.Button(self,text="Home",command=controller.display_page(HomePage))
        #Places the home button in the window
        home_button.pack()
        
        #Creates a GameRecap button
        game_recap_button = tk.Button(self,text="Game Recap",command=controller.display_page(GameRecap))
        #Places the button in the window
        game_recap_button.pack()
        
        #Cretes a rebound stats button
        rebound_stats_button = tk.Button(self,text="Rebound stats",command=controller.display_page(ReboundStats))
        #Places the rebound stats button in the window
        rebound_stats_button.pack()
        
        #Cretes a scoring stats button
        scoring_stats_button = tk.Button(self,text="Scoring stats",command=controller.display_page(ScoringStats))
        #Places the scoring stats button in the window
        scoring_stats_button.pack()
        
        assists_stats_button = tk.Button(self,text="Assists stats",command= controller.display_page(AssistStats))
        #Places the assists stats button in the window
        assists_stats_button.pack()

class AssistStats(tk.Frame):
    """Shows the points socred per quarter by each team.
    
    Args:
        tk.Frame: The frame(window) to display information. 
    """
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,controller)
        label = tk.Label(self,text="Points per team during the game")
        label.pack(pdy=10,padx=10)
        
        #Figure is the graph object itself thats passed in as the first arg
        canvas = tk.FigureCanvasTkAgg(figure,self)
        canvas.show()
        canvas.get_tk_widget().pack()
        
        #Creates the toolbar for the graph
        toolbar = tk.NavigationToolBar2Tk(canvas,self)
        toolbar.update()
        
        #Places the toolbar in the window
        canvas.get_tk_widget().pack()
        
        
        #Cretes a home button
        home_button = tk.Button(self,text="Home",command=controller.display_page(HomePage))
        #Places the home button in the window
        home_button.pack()
        
        #Creates a GameRecap button
        game_recap_button = tk.Button(self,text="Game Recap",command=controller.display_page(GameRecap))
        #Places the button in the window
        game_recap_button.pack()
        
        #Cretes a rebound stats button
        rebound_stats_button = tk.Button(self,text="Rebound stats",command=controller.display_page(ReboundStats))
        #Places the rebound stats button in the window
        rebound_stats_button.pack()
        
        #Cretes a scoring stats button
        scoring_stats_button = tk.Button(self,text="Scoring stats",command=controller.display_page(ScoringStats))
        #Places the scoring stats button in the window
        scoring_stats_button.pack()
        
        assists_stats_button = tk.Button(self,text="Assists stats",command= controller.display_page(AssistStats))
        #Places the assists stats button in the window
        assists_stats_button.pack()


def main():
    root= tk.Tk()   #creates an object from the class defined above
    #size of the window
    root.geometry("400x300")
    app=Window(root)
    app.mainloop() #Gernates the window when the code is executed
    
if __name__ == '__main__':
    main()