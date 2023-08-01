import pandas as pd

data = pd.read_csv("FPL_Schedule2324.csv")

# # Getting each row data
# for index, row in data.iterrows():
#     print(row)

# Filtering
# print(data.loc[data['Team'] == 'Arsenal'])


def getTeamFixtures(team):
    team_fixtures = data.loc[data["Team"] == team.capitalize()]
    gameweeks_dict = {
        col: team_fixtures[col].iloc[0]  # Create a dictionary with gameweek as key and fixture as value
        for col in team_fixtures.columns if col != "Team"  # Exclude the 'Team' column
    }
    team_dict = {
        "Team": team_fixtures["Team"].iloc[0],  # Get the team name from the first row
        "Gameweeks": gameweeks_dict
    }
    return team_dict


print(getTeamFixtures("arsenal"))
