import mlflow
import os

mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))

with open("model_info.txt", "r") as f:
    run_id = f.read().strip()

run = mlflow.get_run(run_id)
accuracy = run.data.metrics["accuracy"]

print("Accuracy:", accuracy)

if accuracy < 0.85:
    raise Exception("Model accuracy below threshold")
else:
    print("Model passed threshold")