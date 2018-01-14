from pymongo import MongoClient
from progressbar import ProgressBar, Bar, Percentage, FormatLabel, ETA
import numpy as np
import os
from sklearn.model_selection import train_test_split

np.set_printoptions(threshold=np.nan)
client = MongoClient(host='localhost', port=27017)
db = client[os.getenv('DOTABOT_DB_NAME', 'dotabot_db')]
match_collection = db.matches

# We're going to create a training matrix, X, where each
# row is a different match and each column is a feature

# The features are bit vectors indicating whether heroes
# were picked (1) or not picked (0). The first N features
# correspond to radiant, and the last N features are
# for dire.

NUM_HEROES = 108
NUM_FEATURES = NUM_HEROES * 2

# Our training label vector, Y, is a bit vector indicating
# whether radiant won (1) or lost (-1)
NUM_MATCHES = match_collection.count()

# Initialize training matrix
X = np.zeros((NUM_MATCHES, NUM_FEATURES), dtype=np.int8)

# Initialize training label vector
Y = np.zeros(NUM_MATCHES, dtype=np.int8)

# progressbar and widget info for commandline
widgets = [FormatLabel('Processed: %(value)d/%(max)d matches. '), ETA(), Percentage(), ' ', Bar()]
pbar = ProgressBar(widgets=widgets, maxval=NUM_MATCHES).start()

for i, record in enumerate(match_collection.find().limit(163905)):
    pbar.update(i)
    if not record['radiant_win']:
        Y[i] = 0
    else: Y[i]= 1
    ''' If the left-most bit of player_slot is set,this player is on dire, so push the index accordingly'''
    for player in record['players']:
        hero_id = player['hero_id'] - 1
        player_slot = player['player_slot']
        if player_slot >= 128:
            hero_id += NUM_HEROES

        X[i, hero_id] = 1

pbar.finish()

print("Permuting, generating train and test sets.")
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=42)
print("Saving output file now...")
np.savez_compressed('data-source/test_%d.npz' % len(X_test), X=X_test, Y=Y_test)
np.savez_compressed('data-source/train_%d.npz' % len(X_train), X=X_train, Y=Y_train)
