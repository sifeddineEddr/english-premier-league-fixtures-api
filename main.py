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
    all_gameweeks = getAllGameweeks()
    team_fixtures = {}

    for gameweek, game_list in all_gameweeks.items():
        for game in game_list:
            if ( team.lower() in game.lower() ):  # I had to use game.lower() for the teams having a white space on their name
                team_fixtures[gameweek] = game

    sorted_team_fixtures = {
        key: value
        for key, value in sorted(team_fixtures.items(), key=lambda x: int(x[0][2:]))
    }

    response = [{gw: fixture} for gw, fixture in sorted_team_fixtures.items()]

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
