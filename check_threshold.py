import mlflow

# read run id
with open("model_info.txt", "r") as f:
    run_id = f.read().strip()

# get run data
client = mlflow.tracking.MlflowClient()
run = client.get_run(run_id)

accuracy = run.data.metrics["accuracy"]

print("Model accuracy:", accuracy)

# check threshold
if accuracy < 0.85:
    raise Exception("Model accuracy below threshold! Failing pipeline.")
else:
    print("Model passed threshold ✅")