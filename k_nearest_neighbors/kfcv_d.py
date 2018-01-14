import numpy as np
from progressbar import ProgressBar, Bar, Percentage, FormatLabel, ETA
from sklearn import model_selection
from sklearn.neighbors import KNeighborsClassifier

global trainset
from sklearn import cross_validation
import joblib


def my_distance(vec1, vec2):
    # return np.sum(np.multiply(vec1,vec2))
    logical_and = np.sum(np.logical_and(vec1, vec2))
    return logical_and


def poly_param(d):
    def poly_weights(distances):
        '''Returns a list of weights given a polynomial weighting function'''
        weights = np.power(np.multiply(distances[0], 0.1), d)
        return np.array([weights])

    return poly_weights


def score(estimator, X, y):
    global pbar, FOLDS_FINISHED
    correct_predictions = 0
    for i, radiant_query in enumerate(X):
        radiant_query = radiant_query.reshape(1, -1)
        pbar.update(FOLDS_FINISHED)
        dire_query = np.concatenate((radiant_query[NUM_HEROES:NUM_FEATURES], radiant_query[0:NUM_HEROES])).reshape(1,
                                                                                                                   -1)
        rad_prob = estimator.predict_proba(radiant_query)[0][1]
        dire_prob = estimator.predict_proba(dire_query)[0][0]
        overall_prob = (rad_prob + dire_prob) / 2
        prediction = 1 if (overall_prob > 0.5) else -1
        result = 1 if prediction == y[i] else 0
        correct_predictions += result
    FOLDS_FINISHED += 1
    accuracy = float(correct_predictions) / len(X)
    print('Accuracy: %f' % accuracy)
    return accuracy


NUM_HEROES = 108
NUM_FEATURES = NUM_HEROES * 2
K = 4
FOLDS_FINISHED = 0

# Import the preprocessed X matrix and Y vector
preprocessed = np.load('data-source/train_110225.npz')
X = preprocessed['X']
Y = preprocessed['Y']

NUM_MATCHES = len(X)
# X = X[0:NUM_MATCHES]
# Y = Y[0:NUM_MATCHES]

print('Training using data from %d matches...' % NUM_MATCHES)
# X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42)
# k_fold = model_selection.StratifiedKFold(n_splits=K,random_state=42,shuffle=True)
k_fold = cross_validation.KFold(NUM_MATCHES, n_folds=K)

d_tries = [3, 4, 5]

widgets = [FormatLabel('Processed: %(value)d/%(max)d folds. '), ETA(), Percentage(), ' ', Bar()]
pbar = ProgressBar(widgets=widgets, maxval=(len(d_tries) * K)).start()

d_accuracy_pairs = []
for d_index, d in enumerate(d_tries):
    model = KNeighborsClassifier(n_neighbors=NUM_MATCHES // K, weights=poly_param(d), metric=my_distance)
    model_accuracies = model_selection.cross_val_score(model, X, Y, scoring=score, cv=k_fold)
    model_accuracy = model_accuracies.mean()
    d_accuracy_pairs.append((d, model_accuracy))
    filename = 'data-source/model_accuracies_%d_folds.sav' % d_index
    joblib.dump(model_accuracies, filename)
    # # Plot the decision boundary. For that, we will assign a color to each
    # # point in the mesh [x_min, x_max]x[y_min, y_max].
    # h = .02
    # # Create color maps
    # cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    # cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
    # x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    # y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    # xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
    #                      np.arange(y_min, y_max, h))
    # Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    #
    # # Put the result into a color plot
    # Z = Z.reshape(xx.shape)
    # plt.figure()
    # plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
    #
    # # Plot also the training points
    # plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=cmap_bold,
    #             edgecolor='k', s=20)
    # plt.xlim(xx.min(), xx.max())
    # plt.ylim(yy.min(), yy.max())
    # plt.title("3-Class classification (k = %i, weights = '%s')"
    #           % (NUM_MATCHES/K, poly_param(d)))

# plt.show()
# pbar.finish()
print(d_accuracy_pairs)
