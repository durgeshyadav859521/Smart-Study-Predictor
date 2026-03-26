import numpy as np
import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def generate_dataset(n=500):
    data = []

    for _ in range(n):
        mood = random.randint(1, 5)
        stress = random.randint(1, 5)
        sleep = random.uniform(3, 10)
        prev_study = random.uniform(0, 6)
        energy = random.randint(1, 5)

        study_time = (
            (sleep * 0.4) +
            (mood * 0.8) -
            (stress * 0.5) +
            (energy * 0.9) +
            (prev_study * 0.3) +
            random.uniform(-1, 1)
        )

        study_time = max(0, min(study_time, 8))  # clamp between 0–8 hours
        data.append([mood, stress, sleep, prev_study, energy, study_time])

    df = pd.DataFrame(data, columns=[
        "mood", "stress", "sleep_hours", "prev_study_hours", "energy", "recommended_study"
    ])
    return df

df = generate_dataset()
print("Dataset sample:")
print(df.head())

X = df[["mood", "stress", "sleep_hours", "prev_study_hours", "energy"]]
y = df["recommended_study"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
pred = model.predict(X_test)
mse = mean_squared_error(y_test, pred)
print("\nModel Trained Successfully!")
print("Mean Squared Error:", mse)
def predict_study_time(mood, stress, sleep, prev_study, energy):
    inp = np.array([[mood, stress, sleep, prev_study, energy]])
    result = model.predict(inp)[0]
    return round(max(0, min(result, 8)), 2)
print("\n--- Smart Study Time Predictor ---")
mood = int(input("Mood (1–5): "))
stress = int(input("Stress (1–5): "))
sleep = float(input("Sleep hours (3–10): "))
prev_study = float(input("Yesterday study hours (0–6): "))
energy = int(input("Energy level (1–5): "))
output = predict_study_time(mood, stress, sleep, prev_study, energy)
print(f"\n🔹 Recommended Study Time Today: {output} hours")