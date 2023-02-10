from nba_api.stats.endpoints import playercareerstats
import pandas as pd

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    career = playercareerstats.PlayerCareerStats(player_id='203999')
    career.get_data_frames()[0]
    r = career.get_json()
    print(r)
