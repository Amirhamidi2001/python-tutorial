# Machine Learning - Cross Validation

from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import (
    KFold,
    cross_val_score,
    StratifiedKFold,
    LeaveOneOut,
    LeavePOut,
    ShuffleSplit,
)


# K-Fold
X, y = datasets.load_iris(return_X_y=True)
clf = DecisionTreeClassifier(random_state=42)
k_folds = KFold(n_splits=5)
scores = cross_val_score(clf, X, y, cv=k_folds)
print("Cross Validation Scores: ", scores)
print("Average CV Score: ", scores.mean())
print("Number of CV Scores used in Average: ", len(scores))

# Stratified K-Fold
X, y = datasets.load_iris(return_X_y=True)
sk_folds = StratifiedKFold(n_splits=5)
scores = cross_val_score(clf, X, y, cv=sk_folds)
print("Cross Validation Scores: ", scores)
print("Average CV Score: ", scores.mean())
print("Number of CV Scores used in Average: ", len(scores))

# Leave-One-Out (LOO)
X, y = datasets.load_iris(return_X_y=True)
clf = DecisionTreeClassifier(random_state=42)
loo = LeaveOneOut()
scores = cross_val_score(clf, X, y, cv=loo)
print("Cross Validation Scores: ", scores)
print("Average CV Score: ", scores.mean())
print("Number of CV Scores used in Average: ", len(scores))

# Leave-P-Out (LPO)
X, y = datasets.load_iris(return_X_y=True)
clf = DecisionTreeClassifier(random_state=42)
lpo = LeavePOut(p=2)
scores = cross_val_score(clf, X, y, cv=lpo)
print("Cross Validation Scores: ", scores)
print("Average CV Score: ", scores.mean())
print("Number of CV Scores used in Average: ", len(scores))

# Shuffle Split
X, y = datasets.load_iris(return_X_y=True)
clf = DecisionTreeClassifier(random_state=42)
ss = ShuffleSplit(train_size=0.6, test_size=0.3, n_splits=5)
scores = cross_val_score(clf, X, y, cv=ss)
print("Cross Validation Scores: ", scores)
print("Average CV Score: ", scores.mean())
print("Number of CV Scores used in Average: ", len(scores))
