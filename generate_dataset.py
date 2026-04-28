import pandas as pd
import random

data = []

# 500 sample transactions
for i in range(500):
    amount = random.randint(100, 50000)
    time = random.randint(0, 23)
    location = random.randint(1, 10)
    merchant = random.randint(1, 10)

    # Basic fraud logic
    fraud = 1 if amount > 20000 or location > 7 else 0

    data.append([amount, time, location, merchant, fraud])

# Create DataFrame
df = pd.DataFrame(
    data,
    columns=["amount", "time", "location", "merchant", "fraud"]
)

# Save CSV
df.to_csv("fraud_dataset.csv", index=False)

print("Dataset Created Successfully!")