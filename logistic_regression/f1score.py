import numpy as np
from sklearn.metrics import precision_recall_fscore_support

from logistic_regression.logistic_regression import D2LogisticRegression

POSITIVE_LABEL = 1
NEGATIVE_LABEL = 0


def make_prediction(algo, query):
    prob = algo.score(query)
    return POSITIVE_LABEL if prob > 0.5 else NEGATIVE_LABEL


algo = D2LogisticRegression(model_root='.')

testing_data = np.load('test_16401.npz')
X = testing_data['X']
Y_true = testing_data['Y']
num_matches = len(Y_true)

Y_pred = np.zeros(num_matches)
for i, match in enumerate(X):
    Y_pred[i] = make_prediction(algo, match)

prec, recall, f1, support = precision_recall_fscore_support(Y_true, Y_pred, average='macro')

print('Precision: ', prec)
print('Recall: ', recall)
print('F1 Score: ', f1)
print('Support: ', support)
"""
The precision is the ratio tp / (tp + fp) where tp is the number of true positives and fp the number of false positives. The precision is intuitively the ability of the classifier not to label as positive a sample that is negative.

The recall is the ratio tp / (tp + fn) where tp is the number of true positives and fn the number of false negatives. The recall is intuitively the ability of the classifier to find all the positive samples.

The F_beta score can be interpreted as a weighted harmonic mean of the precision and recall, where an F_beta score reaches its best value at 1 and worst score at 0.

The F_beta score weights recall beta as much as precision. beta = 1.0 means recall and precsion are equally important.

The support is the number of occurrences of each class in y_true.
"""
# Precision:  0.781616907078
# Recall:  0.68468997943
# F1 Score:  0.729949874687
# Support:  3403
