from flask import Flask, render_template, request
app = Flask(__name__)

teams = [
    {'name': 'ЦСКА София', 'points': 0},
    {'name': 'Лудогорец Разград', 'points': 0},
    {'name': 'Левски София', 'points': 0},
    {'name': 'ЦСКА 1948', 'points': 0},
    {'name': 'Локомотив Пловдив', 'points': 0},
    {'name': 'Черно море Варна', 'points': 0},
    {'name': 'Славия София', 'points': 0},
    {'name': 'Арда Кърджали', 'points': 0}
]

matches = [
    {'round': 1, 'team1': 'Черно море Варна','team2': 'Лудогорец Разград', 'score1': 2, 'score2': 1, 'date': 'Юни 1, 2022'},
    {'round': 1, 'team1': 'ЦСКА София', 'team2': 'Арда Кърджали', 'score1': 3, 'score2': 0, 'date': 'Юни 1, 2022'},
    {'round': 1, 'team1': 'ЦСКА 1948', 'team2': 'Славия София', 'score1': 2, 'score2': 3, 'date': 'Юни 1, 2022'},
    {'round': 1, 'team1': 'Левски София', 'team2': 'Локомотив Пловдив', 'score1': 3, 'score2': 0, 'date': 'Юни 1, 2022'},
    {'round': 2, 'team1': 'Лудогорец Разград', 'team2': 'Локомотив Пловдив', 'score1': 2, 'score2': 0, 'date': 'Юни5, 2022'},
    {'round': 2, 'team1': 'Славия София', 'team2': 'Левски София', 'score1': 0, 'score2': 0, 'date': 'Юни 5, 2022'},
    {'round': 2, 'team1': 'Арда Кърджали', 'team2': 'ЦСКА 1948', 'score1': 0, 'score2': 1, 'date': 'Юни 5, 2022'},
    {'round': 2, 'team1': 'Черно море Варна', 'team2': 'ЦСКА София', 'score1': 0, 'score2': 1, 'date': 'Юни 5, 2022'},
    {'round': 3, 'team1': 'ЦСКА София', 'team2': 'Лудогорец Разград', 'score1': 0, 'score2': 0, 'date': 'Юни 8, 2022'},
    {'round': 3, 'team1': 'ЦСКА 1948', 'team2': 'Черно море Варна', 'score1': 1, 'score2': 0, 'date': 'Юни 8, 2022'},
    {'round': 3, 'team1': 'Левски София', 'team2': 'Арда Кърджали', 'score1': 0, 'score2': 2, 'date': 'Юни 8, 2022'},
    {'round': 3, 'team1': 'Локомотив Пловдив', 'team2': 'Славия София', 'score1': 0, 'score2': 2, 'date': 'Юни 8, 2022'},
    {'round': 4, 'team1': 'Лудогорец Разград', 'team2': 'Славия София', 'score1': 4, 'score2': 1, 'date': 'Юни 20, 2022'},
    {'round': 4, 'team1': 'Арда Кърджали', 'team2': 'Локомотив Пловдив', 'score1': 1, 'score2': 2, 'date': 'Юни 20, 2022'},
    {'round': 4, 'team1': 'Черно море Варна', 'team2': 'Левски София', 'score1': 2, 'score2': 0, 'date': 'Юни 20, 2022'},
    {'round': 4, 'team1': 'ЦСКА София', 'team2': 'ЦСКА 1948', 'score1': 5, 'score2': 1, 'date': 'Юни 20, 2022'},
    {'round': 5, 'team1': 'ЦСКА 1948', 'team2': 'Лудогорец Разград', 'score1': 2, 'score2': 3, 'date': 'Юни 24, 2022'},
    {'round': 5, 'team1': 'Левски София', 'team2': 'ЦСКА София', 'score1': 0, 'score2': 2, 'date': 'Юни 24, 2022'},
    {'round': 5, 'team1': 'Локомотив Пловдив', 'team2': 'Черно море Варна', 'score1': 1, 'score2': 1, 'date': 'Юни24, 2022'},
    {'round': 5, 'team1': 'Славия София', 'team2': 'Арда Кърджали', 'score1': 1, 'score2': 0, 'date': 'Юни 24, 2022'},
    {'round': 6, 'team1': 'Лудогорец Разград', 'team2': 'Арда Кърджали', 'score1': 1, 'score2': 1, 'date': 'Юни 28, 2022'},
    {'round': 6, 'team1': 'Черно море Варна', 'team2': 'Славия София', 'score1': 0, 'score2': 1, 'date': 'Юни 28, 2022'},
    {'round': 6, 'team1': 'ЦСКА София', 'team2': 'Локомотив Пловдив', 'score1': 4, 'score2': 0, 'date': 'Юни 28, 2022'},
    {'round': 6, 'team1': 'ЦСКА 1948', 'team2': 'Левски София', 'score1': 1, 'score2': 0, 'date': 'Юни 28, 2022'},
    {'round': 7, 'team1': 'Левски София', 'team2': 'Лудогорец Разград', 'score1': 2, 'score2': 0, 'date': 'Юли 3, 2022'},
    {'round': 7, 'team1': 'Локомотив Пловдив', 'team2': 'ЦСКА 1948', 'score1': 0, 'score2': 0, 'date': 'Юли 3, 2022'},
    {'round': 7, 'team1': 'Славия София', 'team2': 'ЦСКА София', 'score1': 1, 'score2': 2, 'date': 'Юли 3, 2022'},
    {'round': 7, 'team1': 'Арда Кърджали', 'team2': 'Черно море Варна', 'score1': 1, 'score2': 1, 'date': 'Юли 3, 2022'},
]

initial_points = {team['name']: team['points'] for team in teams}

def update_ranking():
    for team in teams:
        team['points'] = initial_points[team['name']]

    for match in matches:
        if match['score1'] != 0 or match['score2'] != 0:
            team1 = next(team for team in teams if team['name'] == match['team1'])
            team2 = next(team for team in teams if team['name'] == match['team2'])
            if match['score1'] > match['score2']:
                team1['points'] += 3
            elif match['score1'] < match['score2']:
                team2['points'] += 3
            else:
                team1['points'] += 1
                team2['points'] += 1
    teams.sort(key=lambda x: x['points'], reverse=True)

@app.route('/')
def home():
    round_param = request.args.get('round')
    if round_param:
        current_round = int(round_param)
    else:
        current_round = 1

    if current_round == 1:
        update_ranking()
    return render_template('index.html', teams=teams, matches=matches, current_round=current_round, max_round=max_round)

if __name__ == '__main__':
    max_round = max(match['round'] for match in matches)
    app.run()