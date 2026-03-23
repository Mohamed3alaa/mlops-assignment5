import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# load data
X, y = load_iris(return_X_y=True)

# split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# start mlflow run
with mlflow.start_run():
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    # log accuracy to MLflow
    mlflow.log_metric("accuracy", acc)

    print("Accuracy:", acc)

    # save accuracy to file (for pipeline)
    with open("model_info.txt", "w") as f:
        f.write(str(acc))