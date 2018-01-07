from sklearn.linear_model import LogisticRegression
import pickle,json,joblib
import numpy as np

def train(X, Y, num_samples):
    print('Training using data from %d matches...' % num_samples)
    return LogisticRegression().fit(X[0:num_samples], Y[0:num_samples])

def main():
    # Import the preprocessed training X matrix and Y vector
    preprocessed = np.load('train_147615.npz')
    d = dict(zip(("data1{}".format(k) for k in preprocessed), (preprocessed[k] for k in preprocessed)))
    print(d)
    X_train = preprocessed['X']
    Y_train = preprocessed['Y']

    model = train(X_train, Y_train, len(X_train))
    filename = 'finalized_model.sav'
    joblib.dump(model, filename)
    #with open('model.pkl', 'wb') as output_file:
    #    pickle.dump(model, output_file)

if __name__ == "__main__":
    main()
