import pandas as pd
import joblib
from sklearn.neighbors import NearestNeighbors

# -----------------------------
# Load Hotel Dataset
# -----------------------------

hotel_df = pd.read_csv("dataset/hotels.csv")

# -----------------------------
# Load KNN Model
# -----------------------------

try:
    model = joblib.load("hotel_model.pkl")

except:
    X = hotel_df[["Price", "Rating"]]

    model = NearestNeighbors(
        n_neighbors=3,
        metric="euclidean"
    )

    model.fit(X)

# -----------------------------
# Recommend Hotels
# -----------------------------

def recommend_hotels(destination, budget, travellers):

    city_hotels = hotel_df[
        hotel_df["City"].str.lower() == destination.lower()
    ]

    if len(city_hotels) == 0:

        city_hotels = hotel_df

    max_price = budget // max(1, travellers)

    city_hotels = city_hotels[
        city_hotels["Price"] <= max_price
    ]

    if len(city_hotels) == 0:

        city_hotels = hotel_df[
            hotel_df["City"].str.lower() == destination.lower()
        ]

    X = city_hotels[["Price", "Rating"]]

    knn = NearestNeighbors(
        n_neighbors=min(3, len(city_hotels)),
        metric="euclidean"
    )

    knn.fit(X)

    query = [[max_price, 5]]

    distances, indices = knn.kneighbors(query)

    recommendations = city_hotels.iloc[
        indices[0]
    ]

    return recommendations.to_dict("records")


# -----------------------------
# Create Itinerary
# -----------------------------

def create_itinerary(destination, days):

    attraction_df = pd.read_csv(
        "dataset/attractions.csv"
    )

    places = attraction_df[
        attraction_df["City"].str.lower() == destination.lower()
    ]

    if len(places) == 0:

        return "No attractions available."

    places = places.reset_index(drop=True)

    output = ""

    place_no = 0

    for day in range(1, days + 1):

        output += f"""
==================================================
🗓️ DAY {day}
==================================================

🌅 Wake Up : 7:00 AM

🍳 Breakfast : Local Restaurant

"""

        for i in range(2):

            if place_no >= len(places):
                break

            output += f"""📍 Visit : {places.iloc[place_no]["Place"]}

"""

            place_no += 1

        output += """🚕 Transport : Taxi / Auto

🍽️ Lunch : Local Food

🌆 Evening : Shopping

🌙 Dinner : Hotel

"""

    return output