import mlflow

mlflow.set_tracking_uri("file:./mlruns")

with open("model_info.txt", "r") as f:
    run_id = f.read().strip()

client = mlflow.tracking.MlflowClient()
run = client.get_run(run_id)

accuracy = run.data.metrics["accuracy"]

print("Model accuracy:", accuracy)

if accuracy < 0.85:
    raise Exception("Model accuracy below threshold!")
else:
    print("Model passed threshold ✅")