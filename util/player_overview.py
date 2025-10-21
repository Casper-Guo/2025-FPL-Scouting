"""Accept player names from CLI and display summary stastistics."""

import requests
import shutil

import pandas as pd

# columns to display
COLUMNS = [
    "total_points",
    "minutes",
    "goals_scored",
    "expected_goals",
    "expected_goals_per_90",
    "assists",
    "expected_assists",
    "expected_assists_per_90",
    "expected_goal_involvements",
    "expected_goal_involvements_per_90",
    "defensive_contribution",
    "defensive_contribution_per_90",
    "clean_sheets",
    "ict_index_rank",
]


def get_player_row(df: pd.DataFrame, player_name: str) -> pd.Series | None:
    """Get player row from DataFrame based on name match."""
    if player_name not in df["web_name"].values:
        print(f"No matches for {player_name}")
        return None

    if df[df["web_name"] == player_name].shape[0] == 1:
        return df[df["web_name"] == player_name].iloc[0][COLUMNS]

    matches = df[df["web_name"] == player_name].reset_index()
    matches["full_name"] = matches["first_name"] + " " + matches["second_name"]

    options = [f"{index}) {row['full_name']}" for index, row in matches.iterrows()]
    select_prompt = f"Multiple matches - {' '.join(options)}: "
    selection = int(input(select_prompt))
    return matches.iloc[selection][COLUMNS]


def main():
    raw = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/").json()

    fpl_teams = pd.json_normalize(raw["teams"])[["id", "name", "short_name"]].rename(
        columns={"name": "team_name", "short_name": "team_short_name"}
    )
    fpl_positions = pd.json_normalize(raw["element_types"])[
        ["id", "singular_name_short"]
    ].rename(columns={"singular_name_short": "position"})
    fpl_players = pd.json_normalize(raw["elements"])

    df = pd.merge(
        fpl_players,
        fpl_teams,
        left_on="team",
        right_on="id",
        how="left",
        suffixes=(None, "_team"),
    ).drop(columns=["team", "id_team"])

    df = df.merge(
        fpl_positions,
        left_on="element_type",
        right_on="id",
        how="left",
        suffixes=(None, "_position"),
    ).drop(columns=["element_type", "id_position"])

    df = df.set_index("id")

    while True:
        print(f"{'-' * shutil.get_terminal_size().columns}\n")
        try:
            player_web_name = input("Enter player's FPL display name: ")
            if (row := get_player_row(df, player_web_name)) is None:
                continue
            print(row.to_string())
            print()
        except (KeyboardInterrupt, EOFError):
            break


if __name__ == "__main__":
    main()
