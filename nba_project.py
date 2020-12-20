"""A module for the nba_project program main functionality.

Attributes:
    None.
"""

import pandas
import matplotlib.pyplot as plt 
from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamgamelog
from nba_api.stats.endpoints import boxscoresummaryv2
from nba_api.stats.endpoints import infographicfanduelplayer


class nba_teamgame:
    """A class for the NBA game listing (schedule) based on the user's choice of NBA team and season.

    Attributes:
        name (str): the name of the NBA team.
        year (str): the season duration (year) of the NBA team.
    """
    
    def __init__(self, name, year):
        
        self.name = name
        self.year = year
    
    
    
    def team_id(self):
        """Receives the NBA team id based on the user's choice of NBA team and season.

    Args:
        None.

    Returns:
        None.
    """
        
        team_dict = teams.get_teams()
        nbagame = [team for team in team_dict if team["full_name"] == self.name][0]
        nba_id = nbagame["id"]
        self.num = nba_id



    def team_gamelist(self):
        """Present the game listing (schedule) for the specific NBA team and season.

    Args:
        None.

    Returns:
        the game listing (schedule) for the specific NBA team and season.
    """
        
        nbagamelist = teamgamelog.TeamGameLog(season=self.year, season_type_all_star="Regular Season", team_id=self.num)
        nbagamedata = nbagamelist.team_game_log.get_data_frame()
        return nbagamedata[["Game_ID", "MATCHUP"]]
    
    
    
class nba_gamestats:
    """A class for the NBA game information based on the user's choice of NBA matchup.

    Attributes:
        gameid (str): the game id of the specific NBA matchup.
    """
    
    def __init__(self, gameid):
        self.gameid = gameid
    
    
    
    def nbagame_info(self):
        """Present the specific NBA matchup main game information.

    Args:
        None.

    Returns:
        the specific NBA matchup main game information.
    """
        
        nbabasic = boxscoresummaryv2.BoxScoreSummaryV2(game_id=self.gameid)
        nbagame = nbabasic.game_info.get_data_frame()
        nbagameinfo = nbagame[['GAME_DATE', 'ATTENDANCE']]
        return nbagameinfo
    
    
    
    def nbagame_summary(self):
        """Present the specific NBA matchup game summary (box-score).

    Args:
        None.

    Returns:
        the specific NBA matchup game summary (box-score).
    """
        
        nbasummary = boxscoresummaryv2.BoxScoreSummaryV2(game_id=self.gameid)
        nbasum = nbasummary.line_score.get_data_frame()
        nbasummaryinfo = nbasum[['PTS_QTR1', 'PTS_QTR2', 'PTS_QTR3', 'PTS_QTR4']]
        nbasummaryinfo.iloc[0].plot(label = 'Selected Team', kind = 'line') 
        nbasummaryinfo.iloc[1].plot(label = 'Other Team', kind = 'line')
        
        plt.xlabel("NBA Quarters")
        plt.ylabel("NBA Scores (PTS)")
        plt.title("NBA Scoreboard")
        plt.legend()
        plt.show()
        
        return nbasummaryinfo
    
    
    
    def nbagame_summaryscore(self):
        """Present the specific NBA matchup game summary (box-score).

    Args:
        None.

    Returns:
        the specific NBA matchup game summary (point leaders).
    """
        
        nbascore = infographicfanduelplayer.InfographicFanDuelPlayer(game_id=self.gameid)
        nbascoreone = nbascore.fan_duel_player.get_data_frame()
        nbascoreone["Players"] = nbascoreone['PLAYER_NAME'] + " " + "(" + nbascoreone['TEAM_ABBREVIATION'] + ")"
        nbascoretwo = nbascoreone[['Players', 'PTS']].sort_values(by = 'PTS', ascending = False).head(5)
        plt.barh("Players", "PTS", data = nbascoretwo, color = "blue")
        
        plt.xlabel("Number Of Points (PTS)")
        plt.ylabel("NBA Players")
        plt.title("Point Leaders")
        plt.show()
        
        return nbascoretwo
    
    
    
    def nbagame_summaryreb(self):
        """Present the specific NBA matchup game summary (box-score).

    Args:
        None.

    Returns:
        the specific NBA matchup game summary (rebound leaders).
    """
        
        nbareb = infographicfanduelplayer.InfographicFanDuelPlayer(game_id=self.gameid)
        nbarebone = nbareb.fan_duel_player.get_data_frame()
        nbarebone["Players"] = nbarebone['PLAYER_NAME'] + " " + "(" + nbarebone['TEAM_ABBREVIATION'] + ")"
        nbarebtwo = nbarebone[['Players', 'REB']].sort_values(by = 'REB', ascending= False).head(5)
        plt.barh("Players", "REB", data = nbarebtwo, color = "blue")
        
        plt.xlabel("Number Of Rebounds (REB)")
        plt.ylabel("NBA Players")
        plt.title("Rebound Leaders")
        plt.show()
        
        return nbarebtwo


        
    def nbagame_summaryassists(self):
        """Present the specific NBA matchup game summary (box-score).

    Args:
        None.

    Returns:
        the specific NBA matchup game summary (assists leaders).
    """
        
        nbaast = infographicfanduelplayer.InfographicFanDuelPlayer(game_id=self.gameid)
        nbaastone = nbaast.fan_duel_player.get_data_frame()
        nbaastone["Players"] = nbaastone['PLAYER_NAME'] + " " + "(" + nbaastone['TEAM_ABBREVIATION'] + ")"
        nbaasttwo = nbaastone[['Players', 'AST']].sort_values(by = 'AST', ascending= False).head(5)
        plt.barh("Players", "AST", data = nbaasttwo, color = "blue")
        
        plt.xlabel("Number Of Assists (AST)")
        plt.ylabel("NBA Players")
        plt.title("Assist Leaders")
        plt.show()
        
        return nbaasttwo



if __name__ == "__main__":
    """Tip: When testing the functionality of the program, here are the steps to run successfully:
    
    1. Run the code.
    2. Copy the game id of the specific matchup (Ex: 0029700076) and paste it where its ask "Enter NBA Game_ID: "
    
    """
    
    nbateam = input('Enter Team Name (Title Case - Full Name): ')
    nbaseason = input('Enter Team Season (1996 - 2019): ')
    nbag = nba_teamgame(nbateam, nbaseason)
    nbag.team_id()
    print(nbag.team_gamelist())
    
    
    nbagameid = input("Enter NBA Game_ID: ")
    nbatwo = nba_gamestats(nbagameid)
    print(nbatwo.nbagame_info())
    print(nbatwo.nbagame_summary())
    print(nbatwo.nbagame_summaryscore())
    print(nbatwo.nbagame_summaryreb())
    print(nbatwo.nbagame_summaryassists())

    
    
   
    



    
    

    
    

    
