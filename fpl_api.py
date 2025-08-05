import requests
import pandas as pd

raw = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/").json()

fpl_teams = pd.json_normalize(raw["teams"])
fpl_positions = pd.json_normalize(raw["element_types"])
fpl_players = pd.json_normalize(raw["elements"])

fpl_teams.to_csv("raw/fpl_teams_2526.csv", index=False)
fpl_positions.to_csv("raw/fpl_positions_2526.csv", index=False)
fpl_players.to_csv("raw/fpl_players_2526.csv", index=False)
