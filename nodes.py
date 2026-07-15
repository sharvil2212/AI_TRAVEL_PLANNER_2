from recommender import recommend_hotels, create_itinerary


# -------------------------------
# Planner Node
# -------------------------------

def planner_node(state):

    itinerary = create_itinerary(
        destination=state["destination"],
        days=state["days"]
    )

    state["itinerary"] = itinerary

    return state


# -------------------------------
# Hotel Recommendation Node
# -------------------------------

def hotel_node(state):

    hotels = recommend_hotels(
        destination=state["destination"],
        budget=state["budget"],
        travellers=state["travellers"]
    )

    output = ""

    for i, hotel in enumerate(hotels, start=1):

        stars = "⭐" * int(hotel["Rating"])

        output += f"""
==================================================
🏨 HOTEL {i} {stars}
==================================================
📍 Hotel Name      : {hotel["Hotel"]}
💰 Price/Night     : ₹{hotel["Price"]}
⭐ Rating          : {hotel["Rating"]}/5
📌 Address         : {hotel["Address"]}

🎯 Nearby Attractions
• {hotel["Attraction1"]}
• {hotel["Attraction2"]}

"""

    state["hotels"] = output

    return state


# -------------------------------
# Budget Node
# -------------------------------

def budget_node(state):

    hotel = int(state["budget"] * 0.40)

    food = int(state["budget"] * 0.30)

    transport = int(state["budget"] * 0.15)

    shopping = int(state["budget"] * 0.10)

    emergency = state["budget"] - (
        hotel +
        food +
        transport +
        shopping
    )

    state["total_budget"] = f"""
==================================================
             💰 BUDGET BREAKDOWN
==================================================

🏨 Hotel Cost      : ₹{hotel}

🍽️ Food Cost       : ₹{food}

🚕 Transport Cost  : ₹{transport}

🛍️ Shopping        : ₹{shopping}

🚑 Emergency       : ₹{emergency}

--------------------------------------------------
💵 Total Budget    : ₹{state["budget"]}
==================================================
"""

    return state