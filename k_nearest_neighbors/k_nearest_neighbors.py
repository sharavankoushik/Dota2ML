import numpy as np
import pickle, os,joblib

NUM_HEROES = 108
NUM_FEATURES = NUM_HEROES * 2
NUM_IN_QUERY = 0
# Lower this value to speed up recommendation engine
TRAINING_SET_SIZE = 10000

def my_distance(vec1,vec2):
    '''Returns a count of the elements that were 1 in both vec1 and vec2.'''
    return np.sum(np.logical_and(vec1,vec2))

def poly_weights_recommend(distances):
    '''Returns a list of weights for the provided list of distances.'''
    global NUM_IN_QUERY
    distances[0] = np.power(np.multiply(distances[0], NUM_IN_QUERY), 4)
    return distances

def poly_weights_evaluate(distances):
    '''Returns a list of weights for the provided list of distances.'''
    distances[0] = np.power(np.multiply(distances[0], NUM_IN_QUERY), 4)
    return distances
    # weights = np.power(np.multiply(distances[0], 0.1), 15)
    # return np.array([weights])

class D2KNearestNeighbors:
    def __init__(self, model_root='k_nearest_neighbors'):
        recommend_path = os.path.join(model_root, 'recommend_models_%d.sav' % TRAINING_SET_SIZE)
        evaluate_path = os.path.join(model_root, 'evaluate_model_%d.sav' % TRAINING_SET_SIZE)
        print(recommend_path)
        print(evaluate_path)
        self.recommend_models = joblib.load('/Users/kosh/Downloads/Dev/dotaml-master/k_nearest_neighbors/recommend_models_10000.sav')
        self.evaluate_model = joblib.load('/Users/kosh/Downloads/Dev/dotaml-master/k_nearest_neighbors/evaluate_model_10000.sav')

    def transform(self, my_team, their_team):
        X = np.zeros(NUM_FEATURES, dtype=np.int8)
        for hero_id in my_team:
            X[hero_id - 1] = 1
        for hero_id in their_team:
            X[hero_id - 1 + NUM_HEROES] = 1
        return X

    """
       1. Run the algorithm on radiant_query to get radiant_prob, the probability that the radiant team in radiant_query wins the             match.

       2. Construct dire_query by swapping the radiant and dire teams in radiant_query so that the radiant team is now the bottom             half of the feature vector and the dire team is now the top half of the feature vector.

       3. Run the algorithm on dire_query to get dire_prob, the probability that the radiant team in radiant_query loses the match            if it was actually the dire team instead.

       4. Calculate the overall probability overall_prob as the average of radiant_prob and (1 - dire_prob).

       5. Predict the outcome of the match specified by radiant_query as the radiant team winning if overall_prob > 0.5 and as the            dire team winning otherwise.
       """
    def recommend(self, my_team, their_team, hero_candidates):
        '''Returns a list of (hero, probablility of winning with hero added) recommended to complete my_team.'''
        global NUM_IN_QUERY
        NUM_IN_QUERY = len(my_team) + len(their_team) + 1
        team_possibilities = [(candidate, my_team + [candidate]) for candidate in hero_candidates]
        prob_candidate_pairs = []
        for candidate, team in team_possibilities:
            #Flag the enemy team as radiant
            query_radiant = self.transform(team, their_team).reshape(1,-1)
            #Flag the enemy team as dire
            query_dire = self.transform(their_team, team).reshape(1,-1)
            # probability of winning if the enemy team is radiant
            prob_radiant = self.recommend_models[candidate-1].predict_proba(query_radiant)[0][1]
            # probability of winning if the enemy team is dire
            prob_dire = self.recommend_models[candidate-1+NUM_HEROES].predict_proba(query_dire)[0][0]
            prob = (prob_radiant + prob_dire) / 2
            prob_candidate_pairs.append((prob, candidate))
        prob_candidate_pairs = sorted(prob_candidate_pairs, reverse=True)[0:5 - len(my_team)]
        return prob_candidate_pairs

    def score(self, query):
        '''Score the query using the evaluation model, considering both radiant and dire teams.'''
        radiant_query = query.reshape(1,-1)
        dire_query = np.concatenate((radiant_query[NUM_HEROES:NUM_FEATURES], radiant_query[0:NUM_HEROES])).reshape(1,-1)
        rad_prob = self.evaluate_model.predict_proba(radiant_query)[0][1]
        dire_prob = self.evaluate_model.predict_proba(dire_query)[0][0]
        return (rad_prob + (1-dire_prob))/2

    def predict(self, dream_team, their_team):
        '''Returns the probability of the dream_team winning against their_team.'''
        dream_team_query = self.transform(dream_team, their_team)
        return self.score(dream_team_query)
