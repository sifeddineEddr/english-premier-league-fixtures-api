import pandas as pd
from flask import Flask, jsonify

data = pd.read_csv("FPL_Schedule2324.csv")

app = Flask(__name__)

def getAllGameweeks():
    all_gameweeks = {}
    already_printed = set()

    for i in range(1, 39):
        gameweek_column = f"GW{i}"
        gameweeks_data = zip(data["Team"], data[gameweek_column])
        fixtures = []

        # To check if the fixture is already on the dictionnary
        for team, fixture in gameweeks_data:
            fixture_pair_1 = f"{team} vs {fixture}"
            fixture_pair_2 = f"{fixture} vs {team}"
            if (
                fixture_pair_1 not in already_printed
                and fixture_pair_2 not in already_printed
            ):
                fixtures.append(fixture_pair_1)
                already_printed.add(fixture_pair_1)

        all_gameweeks[gameweek_column] = fixtures

    return all_gameweeks

@app.route("/gameweeks")
def gameweeks():    
    return jsonify(getAllGameweeks())


@app.route("/gameweeks/<int:gw>")
def getGameweekFixtures(gw):
    all_gameweeks = getAllGameweeks()
    gameweek_column = f"GW{gw}"
    if gameweek_column in all_gameweeks:
        response = {gameweek_column: all_gameweeks[gameweek_column]}
        return jsonify(response)
    else:
        return "Resource not found"


@app.route("/gameweeks/<string:team>")
def getTeamFixtures(team):
    team_fixtures = data.loc[data["Team"] == team.capitalize()]
    gameweeks_dict = {
        col: team_fixtures[col].iloc[0]  # Create a dictionary with gameweek as key and fixture as value
        for col in team_fixtures.columns
        if col != "Team"  # Exclude the 'Team' column
    }
    team_dict = {
        "Team": team_fixtures["Team"].iloc[0],  # Get the team name from the first row
        "Gameweeks": gameweeks_dict,
    }
    return jsonify(team_dict)


if __name__ == "__main__":
    app.run(debug=True)
