import pandas as pd
import joblib

from sklearn.neighbors import NearestNeighbors

# ----------------------------------
# Load Dataset
# ----------------------------------

hotel_df = pd.read_csv("dataset/hotels.csv")

# ----------------------------------
# Features
# ----------------------------------

X = hotel_df[["Price", "Rating"]]

# ----------------------------------
# Train KNN Model
# ----------------------------------

knn = NearestNeighbors(
    n_neighbors=3,
    metric="euclidean"
)

knn.fit(X)

# ----------------------------------
# Save Model
# ----------------------------------

joblib.dump(knn, "hotel_model.pkl")

print("=" * 50)
print("✅ KNN MODEL TRAINED SUCCESSFULLY")
print("📁 File Saved : hotel_model.pkl")
print("=" * 50)