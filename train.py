import mlflow
import random
import os

mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))

with mlflow.start_run() as run:
    accuracy = random.uniform(0.7, 0.95)

    mlflow.log_metric("accuracy", accuracy)

    run_id = run.info.run_id

    print("Accuracy:", accuracy)
    print("Run ID:", run_id)

    with open("model_info.txt", "w") as f:
        f.write(run_id)