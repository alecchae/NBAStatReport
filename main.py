import sys
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players
import pandas as pd

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input = sys.argv[1] + " " + sys.argv[2]
    print(input)
    career = playercareerstats.PlayerCareerStats(player_id='203999')
    r = career.get_data_frames()[0]
    nba_players = players.get_players()

    big_fundamental = [player for player in nba_players
                       if player['full_name'] == input]
    print("player id = " + str(big_fundamental[0]['id']))

