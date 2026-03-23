# read accuracy from file
with open("model_info.txt", "r") as f:
    accuracy = float(f.read().strip())

print("Model accuracy:", accuracy)

# check threshold
if accuracy < 0.85:
    raise Exception("Model accuracy below threshold! Failing pipeline.")
else:
    print("Model passed threshold ✅")