from graph import graph

print("=" * 60)
print("          ✈️ AI TRAVEL PLANNER (KNN) ✈️")
print("=" * 60)

destination = input("🌍 Destination   : ").strip()

days = int(input("📅 Days          : "))

budget = int(input("💰 Budget (₹)    : "))

travellers = int(input("👥 Travellers    : "))

state = {
    "destination": destination,
    "days": days,
    "budget": budget,
    "travellers": travellers,
    "itinerary": "",
    "hotels": "",
    "total_budget": ""
}

result = graph.invoke(state)

print("\n")
print("=" * 60)
print("🗺️ ITINERARY")
print("=" * 60)
print(result["itinerary"])

print("\n")
print("=" * 60)
print("🏨 HOTEL RECOMMENDATIONS")
print("=" * 60)
print(result["hotels"])

print(result["total_budget"])