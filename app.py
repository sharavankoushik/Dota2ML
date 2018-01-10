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

""" """
def get_api_string(recommendations, prob):
    recommendations = list(map(str, recommendations))
    X = json.dumps({'data': recommendations, 'prob_x': prob})
    return X

'''Choose the Engine to run the stats on '''
#engine = Engine(D2LogisticRegression())
engine = Engine(D2KNearestNeighbors())
@app.route('/api/recommend', methods = ['POST'])
def recommend():
    content = request.json
    print(content['x'])
    my_team = content['x']
    their_team = content['y']

    prob_recommendation_pairs = engine.recommend(my_team, their_team)
    recommendations = [hero for prob, hero in prob_recommendation_pairs]
    print(recommendations)
    print([prob for prob,hero in prob_recommendation_pairs])
    prob = engine.predict(my_team, their_team)
    print(prob)
    return get_api_string(recommendations, prob)
if __name__ == '__main__':
    app.run(use_reloader=True,port=5000,threaded=True,debug=True)
