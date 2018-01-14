from flask import Flask, render_template, request
from k_nearest_neighbors.k_nearest_neighbors import D2KNearestNeighbors, my_distance, poly_weights_recommend, poly_weights_evaluate
from logistic_regression.logistic_regression import D2LogisticRegression
from engine import Engine
import json

URL_PREFIX = ''

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def get_api_string(recommendations, prob):
    recommendations = list(map(str, recommendations))
    X = json.dumps({'x': recommendations, 'prob_x': prob})
    return X
'''Choose the Engine to run the stats on '''
#engine = Engine(D2LogisticRegression())
engine = Engine(D2KNearestNeighbors())

@app.route(URL_PREFIX + "/api/suggest/")
def api():
    if 'x' not in request.args or 'y' not in request.args:
        return 'Invalid request'
    my_team = request.args['x'].split(',')
    if len(my_team) == 1 and my_team[0] == '':
        my_team = []
    else:
        my_team = list(map(int, my_team))
    their_team = request.args['y'].split(',')
    if not 1<len(their_team)<=5:
        raise ValueError("Please Select a Hero")
    elif len(their_team) == 1 and their_team[0] == '':
        their_team = []
    else:
        their_team = list(map(int, their_team))
    prob_recommendation_pairs = engine.recommend(my_team, their_team)
    recommendations = [hero for prob, hero in prob_recommendation_pairs]
    print(recommendations)
    print([prob for prob,hero in prob_recommendation_pairs])
    prob = engine.predict(my_team, their_team)
    print(prob)
    return get_api_string(recommendations, prob)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Development Server Help')
    parser.add_argument("-d", "--debug", action="store_true", dest="debug_mode",
                        help="run in debug mode (for use with PyCharm)", default=False)
    parser.add_argument("-p", "--port", dest="port",
                        help="port of server (default:%(default)s)", type=int, default=5000)
    cmd_args = parser.parse_args()
    app_options = {"port": cmd_args.port}

    if cmd_args.debug_mode:
        app_options["debug"] = True
        app_options["use_debugger"] = False
        app_options["use_reloader"] = True

    app.run(**app_options)
