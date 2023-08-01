import pandas as pd
from flask import Flask, jsonify, request

data = pd.read_csv("FPL_Schedule2324.csv")

app = Flask(__name__)


def getAllGameweeks():
    all_gameweeks = {}

    for i in range(1, 39):
        already_printed = set()
        gameweek_column = f"GW{i}"
        gameweeks_data = zip(data["Team"], data[gameweek_column])
        fixtures = []

        # To check if the fixture is already on the dictionary
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
    all_gameweeks = getAllGameweeks()
    response = []

    for gameweek, fixtures in all_gameweeks.items():
        response.append({gameweek: fixtures})

    return jsonify(response)


@app.route("/gameweeks/<int:gw>")
def getGameweekFixtures(gw):
    all_gameweeks = getAllGameweeks()
    gameweek_column = f"GW{gw}"
    if gameweek_column in all_gameweeks:
        response = {gameweek_column: all_gameweeks[gameweek_column]}
        return jsonify(response)
    else:
        return jsonify({"error": "Resource not found"}), 404


@app.route("/gameweeks/<string:team>")
def getTeamFixtures(team):
    team = request.args.get("team", "").strip()  # Get the team name from the 'team' query parameter (url: "http://127.0.0.1:5000/gameweeks?team=arsenal")
    if not team:
        return (jsonify({"error": "Team not specified"}), 400)

    team_fixtures = data.loc[data["Team"] == team.capitalize()]
    if not team_fixtures.empty:
        gameweeks_dict = {
            col: team_fixtures[col].iloc[0]  # Create a dictionary with gameweek as key and fixture as value
            for col in team_fixtures.columns
            if col != "Team"  # Exclude the Team column
        }
        team_dict = {
            "Team": team_fixtures["Team"].iloc[0],  # Get the team name from the first row
            "Gameweeks": gameweeks_dict,
        }
        return jsonify(team_dict)
    else:
        return jsonify({"error": "Team not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
