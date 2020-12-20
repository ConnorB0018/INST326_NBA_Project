"""A module for the nba_project program (GUI Interface).

Attributes:
    None.
"""

import tkinter as tk
import nba_project as np


def main():
    """The main functionality of the GUI Interface.

    Args:
        None.

    Returns:
        None.
    """
    
    root = tk.Tk()
    
    def gameplots(args):
        """Generate the data visualizations for the specific NBA matchup.

    Args:
        args (int): the numbers argument for the corresponding plots.

    Returns:
        None.
    """
    
        nba_gplots = np.nba_gamestats(nbauser_input3.get())
    
        if args == 1:
            nba_gplots.nbagame_summary()
        elif args == 2:
            nba_gplots.nbagame_summaryscore()
        elif args == 3:
            nba_gplots.nbagame_summaryreb()
        elif args == 4:
            nba_gplots.nbagame_summaryassists()
    
    
    nba_button2 = tk.Button(root, text = "Box-Score", command = lambda:gameplots(1))
    nba_button3 = tk.Button(root, text = "Score Leaders", command = lambda:gameplots(2))
    nba_button4 = tk.Button(root, text = "Rebound Leaders", command = lambda:gameplots(3))
    nba_button5 = tk.Button(root, text = "Assist Leaders", command = lambda:gameplots(4))


    nbauser_team3 = tk.Label(root, text = 'Enter NBA Game_ID')
    nbauser_team3.place(x = 175, y = 125, anchor = "center")
    nbauser_team3.pack()
    nbauser_input3 = tk.Entry(root)
    nbauser_input3.pack()
    
    
    nba_button2.pack()
    nba_button3.pack()
    nba_button4.pack()
    nba_button5.pack()

  
    root.title("NBA Score Visualizer Program") 
    
    root.geometry('250x250') 

    root.mainloop()
    
    

if __name__ == "__main__":
    """Tip: When testing the functionality of the GUI program, here are the steps to run successfully:
    
    1. Run the code.
    2. Copy the game id of the specific matchup (Ex: 0029700076) and paste it where its ask "Enter NBA Game_ID: " on the GUI window.
    3. Click one of the buttons to generate the specific visualization regarding the NBA matchup (before clicking the other buttons, close
    the current plot and then click the other button.) 
    
    """
    
    nbateams_userinput = input('Enter Team Name (Title Case - Full Name): ')
    nbaseasons_userinput = input('Enter Team Season (1996 - 2019): ')
    nbajam_input = np.nba_teamgame(nbateams_userinput, nbaseasons_userinput)
    nbajam_input.team_id()
    print(nbajam_input.team_gamelist())
    
    main()
    
    
    