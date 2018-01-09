from logistic_regression.logistic_regression import D2LogisticRegression
from k_nearest_neighbors.k_nearest_neighbors import D2KNearestNeighbors

lr_model = D2LogisticRegression
knn_model = D2KNearestNeighbors

lr_model.fit(X_train, y_train)
knn_model.fit(X_train, y_train)

lr_predict_probabilities = lr_model.predict_proba(X_test)[:,1]

lr_fpr, lr_tpr, _ = roc_curve(y_test, lr_predict_probabilities)
lr_roc_auc = auc(lr_fpr, lr_tpr)

plt.figure()
plt.plot(fpr, tpr, color='darkorange',
         lw=2, label='K-nearest Neighbours (area = %0.2f)' % roc_auc)
plt.plot(lr_fpr, lr_tpr, color='darkgreen',
         lw=2, label='Logistic Regression (area = %0.2f)' % lr_roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc="lower right")
plt.show()