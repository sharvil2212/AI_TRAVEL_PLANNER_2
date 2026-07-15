# ✈️ AI Travel Planner using K-Nearest Neighbors (KNN)

## 📌 Project Overview

AI Travel Planner is a dataset-based Machine Learning project that recommends hotels and generates travel itineraries based on the user's destination, budget, number of days, and number of travellers.

Unlike API-based travel planners, this project works completely offline using a dataset and the K-Nearest Neighbors (KNN) algorithm.

---

## 🎯 Objectives

- Recommend the best hotels based on budget.
- Generate a day-wise travel itinerary.
- Calculate budget distribution.
- Demonstrate the use of Machine Learning without any API.

---

## 🤖 AI/ML Algorithm Used

### K-Nearest Neighbors (KNN)

KNN is used to recommend the most suitable hotels by comparing:

- Hotel Price
- Hotel Rating

The algorithm calculates the Euclidean Distance between hotels and recommends the nearest matching hotels.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Joblib
- LangGraph

---

## 📂 Project Structure

```
AI_Travel_Planner/
│
├── dataset/
│   ├── hotels.csv
│   └── attractions.csv
│
├── train_model.py
├── recommender.py
├── graph.py
├── nodes.py
├── state.py
├── main.py
├── hotel_model.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset

### Hotels Dataset

Contains:

- Hotel Name
- City
- Price
- Rating
- Address
- Nearby Attractions

### Attractions Dataset

Contains:

- City
- Tourist Places

---

## ⚙️ Installation

Clone the repository.

```bash
git clone https://github.com/sharvil2212/AI_TRAVEL_PLANNER.git
```

Go inside the project folder.

```bash
cd AI_TRAVEL_PLANNER
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Model

Run:

```bash
python train_model.py
```

This generates:

```
hotel_model.pkl
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 💻 Sample Input

```
Destination : Goa
Days : 3
Budget : 15000
Travellers : 2
```

---

## 📋 Sample Output

```
==================================================
✈️ AI TRAVEL PLANNER
==================================================

🗺️ ITINERARY

Day 1
Visit Baga Beach
Visit Fort Aguada

--------------------------------------------------

🏨 HOTEL RECOMMENDATIONS

Hotel Green Leaf ⭐⭐⭐⭐

₹1200

--------------------------------------------------

💰 BUDGET

Hotel Cost : ₹6000
Food Cost : ₹4500
Transport : ₹2250
Shopping : ₹1500
Emergency : ₹750
```

---

## 🧠 Machine Learning Workflow

```
User Input
      │
      ▼
Hotel Dataset
      │
      ▼
Feature Selection
(Price, Rating)
      │
      ▼
KNN Algorithm
      │
      ▼
Nearest Hotels
      │
      ▼
Hotel Recommendation
```

---

## 📈 Machine Learning Features

- K-Nearest Neighbors (KNN)
- Euclidean Distance
- Dataset-Based Recommendation
- Budget-Based Filtering
- City-Based Filtering

---

## 📜 License

This project is developed for educational purposes.