"""A module for the NBA project's unit-test."""

import unittest
import pandas
import matplotlib.pyplot as plt 
from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamgamelog
from nba_project import nba_teamgame
from nba_project import nba_gamestats
from nba_api.stats.endpoints import boxscoresummaryv2 

class nba_teamgameTestCase(unittest.TestCase):
    def setUp(self):
        self.nba_teamgame = nba_teamgame("Chicago Bulls","2010")
        self.nba_teamgame.team_id()

    def test_team_id(self):
        self.nba_teamgame.team_id()
        self.assertEqual((self.nba_teamgame.num),1610612741,'incorrect team number')
    
    def test_team_gamelist(self):
        gamedata=self.nba_teamgame.team_gamelist() 
    
        self.assertEqual(gamedata.loc[0,"Game_ID"],"0021001222",'incorrect game id')
        self.assertEqual(gamedata.loc[0,"MATCHUP"],"CHI vs. NJN",'incorrect matchup teams')


class nba_gamestatsTestCase(unittest.TestCase):
    def setUp(self):
        self.nba_gamestats = nba_gamestats("0021001222")
        self.nba_gamestats 

    def test_nbagame_info(self):
        gamedata2=self.nba_gamestats.nbagame_info()
        
        self.assertEqual(gamedata2.loc[0,'GAME_DATE'],"WEDNESDAY, APRIL 13, 2011",'incorrect game date info')
        self.assertEqual(gamedata2.loc[0,'ATTENDANCE'],22420,'incorrect attendance')
    
    def test_nbagame_summary(self):
        gamedata3=self.nba_gamestats.nbagame_summary()
        
        self.assertEqual(gamedata3.loc[0,'PTS_QTR1'], 26,'Selected team incorrect quarter1 points')
        self.assertEqual(gamedata3.loc[0,'PTS_QTR2'], 24,'Selected team incorrect quarter2 points')
        self.assertEqual(gamedata3.loc[0,'PTS_QTR3'], 18,'Selected team incorrect quarter3 points')
        self.assertEqual(gamedata3.loc[0,'PTS_QTR4'], 29,'Selected team incorrect quarter4 points')

        self.assertEqual(gamedata3.loc[1,'PTS_QTR1'], 20,'Other team incorrect quarter1 points')
        self.assertEqual(gamedata3.loc[1,'PTS_QTR2'], 23,'Other team incorrect quarter2 points')
        self.assertEqual(gamedata3.loc[1,'PTS_QTR3'], 25,'Other team incorrect quarter3 points')
        self.assertEqual(gamedata3.loc[1,'PTS_QTR4'], 24,'Other team incorrect quarter4 points')

    def test_nbagame_summaryscore(self):
        gamedata4=self.nba_gamestats.nbagame_summaryscore()
        
        self.assertEqual(gamedata4.loc[11, 'Players'], 'Jordan Farmar (NJN)','incorrect player')
        self.assertEqual(gamedata4.loc[11, 'PTS'], 21,'incorrect points for Jordan Farmar (NJN)')

        self.assertEqual(gamedata4.loc[1, 'Players'], 'Kyle Korver (CHI)','incorrect player')
        self.assertEqual(gamedata4.loc[1, 'PTS'], 19,'incorrect points for Kyle Korver (CHI)')

        self.assertEqual(gamedata4.loc[13, 'Players'], 'Brook Lopez (NJN)','incorrect player')
        self.assertEqual(gamedata4.loc[13, 'PTS'], 17,'incorrect points for Brook Lopez (NJN)')

        self.assertEqual(gamedata4.loc[4, 'Players'], 'Derrick Rose (CHI)','incorrect player')
        self.assertEqual(gamedata4.loc[4, 'PTS'], 15,'incorrect points for Derrick Rose (CHI)')

        self.assertEqual(gamedata4.loc[12, 'Players'], 'Johan Petro (NJN)','incorrect player')
        self.assertEqual(gamedata4.loc[12, 'PTS'], 13,'incorrect points for Johan Petro (NJN)')
        

    def test_nbagame_summaryreb(self):
        gamedata5=self.nba_gamestats.nbagame_summaryreb()
        
        self.assertEqual(gamedata5.loc[0,'Players'], 'Joakim Noah (CHI)','incorrect player')
        self.assertEqual(gamedata5.loc[0, 'REB'],10,'incorrect rebound for Joakim Noah (CHI)')

        self.assertEqual(gamedata5.loc[2,'Players'], 'Taj Gibson (CHI)','incorrect player')
        self.assertEqual(gamedata5.loc[2, 'REB'],8,'incorrect rebound for Taj Gibson (CHI)')

        self.assertEqual(gamedata5.loc[12,'Players'], 'Johan Petro (NJN)','incorrect player')
        self.assertEqual(gamedata5.loc[12, 'REB'],8,'incorrect rebound for Johan Petro (NJN)')

        self.assertEqual(gamedata5.loc[17,'Players'], 'Dan Gadzuric (NJN)','incorrect player')
        self.assertEqual(gamedata5.loc[17, 'REB'],7,'incorrect rebound for Dan Gadzuric (NJN)')

        self.assertEqual(gamedata5.loc[3,'Players'], 'Luol Deng (CHI)','incorrect player')
        self.assertEqual(gamedata5.loc[3, 'REB'],6,'incorrect  rebound for Luol Deng (CHI)')
        
        

    def test_nbagame_summaryassist(self):
        gamedata7=self.nba_gamestats.nbagame_summaryassists()
        
        self.assertEqual(gamedata7.loc[11,'Players'], 'Jordan Farmar (NJN)','incorrect player')
        self.assertEqual(gamedata7.loc[11, 'AST'],12,'incorrect assists for Jordan Farmar (NJN)')

        self.assertEqual(gamedata7.loc[5,'Players'], 'C.J. Watson (CHI)','incorrect player')
        self.assertEqual(gamedata7.loc[5, 'AST'],6,'incorrect assists C.J. Watson (CHI)')

        self.assertEqual(gamedata7.loc[14,'Players'], 'Sasha Vujacic (NJN)','incorrect player')
        self.assertEqual(gamedata7.loc[14, 'AST'],4,'incorrect assists for Sasha Vujacic (NJN)')

        self.assertEqual(gamedata7.loc[1,'Players'], 'Kyle Korver (CHI)','incorrect player')
        self.assertEqual(gamedata7.loc[1, 'AST'],4,'incorrect assist for Kyle Korver (CHI)')

        self.assertEqual(gamedata7.loc[9,'Players'], 'Keith Bogans (CHI)','incorrect player')
        self.assertEqual(gamedata7.loc[9, 'AST'],3,'incorrect assists for Keith Bogans (CHI)')

        
    
if __name__ == '__main__':
    unittest.main()