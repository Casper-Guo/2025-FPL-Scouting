import soccerdata as sd
import pandas as pd

def flatten_fbref_tables(df: pd.DataFrame) -> pd.DataFrame:
    """Flatten row and column label multi-indices."""
    df = df.reset_index()
    df.columns = ['_'.join(col).strip('_') if isinstance(col, tuple) else col for col in df.columns]
    return df

fbref = sd.FBref(leagues="ENG-Premier League", seasons=2024)

fbref_standard = flatten_fbref_tables(fbref.read_player_season_stats(stat_type="standard"))
fbref_shooting = flatten_fbref_tables(fbref.read_player_season_stats(stat_type="shooting"))
fbref_passing = flatten_fbref_tables(fbref.read_player_season_stats(stat_type="passing"))
fbref_passing_types = flatten_fbref_tables(fbref.read_player_season_stats(stat_type="passing_types"))
fbref_goal_shot_creation = flatten_fbref_tables(fbref.read_player_season_stats(stat_type="goal_shot_creation"))
fbref_defense = flatten_fbref_tables(fbref.read_player_season_stats(stat_type="defense"))
fbref_possession = flatten_fbref_tables(fbref.read_player_season_stats(stat_type="possession"))
fbref_possession = flatten_fbref_tables(fbref.read_player_season_stats(stat_type="possession"))
fbref_playing_time = flatten_fbref_tables(fbref.read_player_season_stats(stat_type="playing_time"))
fbref_misc = flatten_fbref_tables(fbref.read_player_season_stats(stat_type="misc"))
fbref_keeper = flatten_fbref_tables(fbref.read_player_season_stats(stat_type="keeper"))
fbref_keeper_adv = flatten_fbref_tables(fbref.read_player_season_stats(stat_type="keeper_adv"))

fbref_standard.to_csv("raw/fbref_standard.csv", index=False)
fbref_shooting.to_csv("raw/fbref_shooting.csv", index=False)
fbref_passing.to_csv("raw/fbref_passing.csv", index=False)
fbref_passing_types.to_csv("raw/fbref_passing_types.csv", index=False)
fbref_goal_shot_creation.to_csv("raw/fbref_goal_shot_creation.csv", index=False)
fbref_defense.to_csv("raw/fbref_defense.csv", index=False)
fbref_possession.to_csv("raw/fbref_possession.csv", index=False)
fbref_playing_time.to_csv("raw/fbref_playing_time.csv", index=False)
fbref_misc.to_csv("raw/fbref_misc.csv", index=False)
fbref_keeper.to_csv("raw/fbref_keeper.csv", index=False)
fbref_keeper_adv.to_csv("raw/fbref_keeper_adv.csv", index=False)
