import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from catboost import CatBoostClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import cross_val_score

def XGBoost():
    data = pd.read_csv('Data.csv')
    x = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values

    # Training set and Test set
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    # Training XGBoost on the Training set
    classifier = XGBClassifier()
    classifier.fit(x_train, y_train)

    # Making the Confusion Matrix
    y_pred = classifier.predict(x_test)
    cm = confusion_matrix(y_test, y_pred)
    ac = accuracy_score(y_test, y_pred)
    print(cm)
    print(ac)

    # Applying k_Fold Cross Validation
    accuracies = cross_val_score(estimator=classifier, X=x_train, y=y_train, cv=10)
    print("Accuracy: {:.2f} %".format(accuracies.mean() * 100))
    print("Standard Deviation: {:.2f} %".format(accuracies.std() * 100))
    
if __name__ == '__main__':
    XGBoost()
