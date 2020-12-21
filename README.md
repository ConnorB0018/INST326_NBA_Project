# NBA Score Visualizer Program (INST 326 - Group 7)
### _Group Members : Matthew Makonnen, Connor Beaudoin, Moses Nyirinkindi, Eric Evan Topmiller_

### Introduction
- The NBA Score Visualizer Program is a visualization application (python program) that allows users to access and generate data visualizations of various components of the Box Score for different NBA matchups. 

### How To Run The Program

Packages to install before running the program files:
- pandas
- matplotlib
- tkinter
- nba_api (https://github.com/swar/nba_api)

Steps of running the program (_nba_project.py_):
1. Download the _nba_project.py_ python file.
2. Open and run the downloaded file through the Command Prompt (CMD). 
3. Enter the NBA Team Full-Name (Ex: Chicago Bulls).
4. Enter the NBA Season/Year (Ex: 2012).
5. Find the specific NBA matchup you want to see and copy the Game_ID (Ex: 0029700076) that is next to the matchup.
6. Paste the Game_ID to where it states "Enter NBA Game_ID: ".

Steps of running the program (_nbaproject_gui_v2.py_):
1. Download both the _nba_project.py_ and _nbaproject_gui_v2.py_ python files in the same folder.
2. Open and run the downloaded file _nbaproject_gui_v2.py_ from the folder through the Command Prompt (CMD).
3. Enter the NBA Team Full-Name (Ex: Chicago Bulls).
4. Enter the NBA Season/Year (Ex: 2012).
5. Find the specific NBA matchup you want to see and copy the Game_ID (Ex: 0029700076) that is next to the matchup.
6. Paste the Game_ID to where it states "Enter NBA Game_ID: " on the GUI window.
7. Click one of the buttons to generate the specific visualization regarding the NBA matchup (before clicking the other buttons, close the current plot and then click the other button.). 

### How To Interpret The Output Of The Program

- The main goal of the NBA Score Visualizer Program is to provide users (NBA fans) access to an in-depth analysis of different NBA matches, without the hassle of reading or sighting complex box score layouts.
- When running the program, the output of the various graphical visualizations and plots varies in interpretation. Here is the rundown of the visualizations' outputted when running the NBA Score Visualizer Program.
  - __Box-Score:__ A line-plot that showcases the quarter-by-quarter NBA scoreboard for the specific matchup.
  - __Score Leaders:__ A bar-chart that showcases the top five scorers (point leaders) of the specific NBA matchup.
  - __Rebound Leaders:__ A bar-chart that showcases the top five rebounders (rebound leaders) of the specific NBA matchup.
  - __Assist Leaders:__ A bar-chart that showcases the top five assisters (assist leaders) of the specific NBA matchup.

### Annotated Bibliography

Swar. “Swar/nba_api.” GitHub, github.com/swar/nba_api. 
  
> Swar's nba_api is an API package that extracts various up-to-date basketball (NBA) box score stats, ranging from a franchise's amount of NBA finals appearance to a listing of NBA players that shoot 90 percent from the 3pt line, from the NBA.com website. With the main goal of the program being to provide users (NBA fans) access to an in-depth analysis of different NBA matches (without the hassle of reading or sighting complex box score layouts), the use of static and endpoint functions within the API helped extract the essential NBA insights and stats needed to produce the information for the program.
