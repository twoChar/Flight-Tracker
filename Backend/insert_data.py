import pymongo
from datetime import datetime

# Establish a connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create or switch to the 'flight_data' database
db = client["flight_data"]

# Create or switch to the 'flights' collection
collection = db["flights"]


# Define your flight data
flight_data = [
    {
        "flight_id": "6E 2341",
        "airline": "Indigo",
        "status": "On Time",
        "departure_gate": "A12",
        "arrival_gate": "B7",
        "scheduled_departure": datetime(2024, 7, 26, 14, 0),
        "scheduled_arrival": datetime(2024, 7, 26, 18, 0),
        "actual_departure": None,
        "actual_arrival": None,
    },
    {
        "flight_id": "6E 2342",
        "airline": "Indigo",
        "status": "Delayed",
        "departure_gate": "C3",
        "arrival_gate": "D4",
        "scheduled_departure": datetime(2024, 7, 26, 16, 0),
        "scheduled_arrival": datetime(2024, 7, 26, 20, 0),
        "actual_departure": None,
        "actual_arrival": None,
    },
    {
      "flight_id": "6E 2344",
      "airline": "Indigo",
      "status": "On Time",
      "departure_gate": "G5",
      "arrival_gate": "H2",
      "scheduled_departure": "2024-07-26T10:00:00Z",
      "scheduled_arrival": "2024-07-26T14:00:00Z",
      "actual_departure": None,
      "actual_arrival": None
    },
    {
      "flight_id": "6E 2345",
      "airline": "Indigo",
      "status": "Delayed",
      "departure_gate": "I1",
      "arrival_gate": "J3",
      "scheduled_departure": "2024-07-26T15:00:00Z",
      "scheduled_arrival": "2024-07-26T19:00:00Z",
      "actual_departure": None,
      "actual_arrival": None
    },
    {
      "flight_id": "6E 2346",
      "airline": "Indigo",
      "status": "On Time",
      "departure_gate": "K7",
      "arrival_gate": "L4",
      "scheduled_departure": "2024-07-26T18:00:00Z",
      "scheduled_arrival": "2024-07-26T22:00:00Z",
      "actual_departure": None,
      "actual_arrival": None
    },
    {
      "flight_id": "6E 2347",
      "airline": "Indigo",
      "status": "Cancelled",
      "departure_gate": "M8",
      "arrival_gate": "N6",
      "scheduled_departure": "2024-07-26T09:00:00Z",
      "scheduled_arrival": "2024-07-26T13:00:00Z",
      "actual_departure": None,
      "actual_arrival": None
    },
    {
      "flight_id": "6E 2348",
      "airline": "Indigo",
      "status": "Delayed",
      "departure_gate": "O4",
      "arrival_gate": "P2",
      "scheduled_departure": "2024-07-26T17:00:00Z",
      "scheduled_arrival": "2024-07-26T21:00:00Z",
      "actual_departure": None,
      "actual_arrival": None
    },
    {
      "flight_id": "6E 2349",
      "airline": "Indigo",
      "status": "On Time",
      "departure_gate": "Q3",
      "arrival_gate": "R1",
      "scheduled_departure": "2024-07-26T11:00:00Z",
      "scheduled_arrival": "2024-07-26T15:00:00Z",
      "actual_departure": None,
      "actual_arrival": None
    },
    {
      "flight_id": "6E 2350",
      "airline": "Indigo",
      "status": "On Time",
      "departure_gate": "S2",
      "arrival_gate": "T5",
      "scheduled_departure": "2024-07-26T13:00:00Z",
      "scheduled_arrival": "2024-07-26T17:00:00Z",
      "actual_departure": None,
      "actual_arrival": None
    },
    # Add other flights similarly
]

# Insert the data into the collection
collection.insert_many(flight_data)
# collection.insert_many(flight_data)

print("Data inserted successfully!")

collection2 = db["notifications"]
notification_data = [
  {
       "notification_id": "1",
       "flight_id": "6E 2341",
       "message": "Your flight 6E 2341 is on time. Departure gate: A12.",
       "timestamp": "2024-07-26T13:00:00Z",
       "method": "SMS",
       "recipient": "+1234567890"
   },
   {
       "notification_id": "2",
       "flight_id": "6E 2342",
       "message": "Your flight 6E 2342 is delayed. New departure time: 2024-07-26T17:00:00Z. Departure gate: C3.",
       "timestamp": "2024-07-26T15:30:00Z",
       "method": "Email",
       "recipient": "user@example.com"
   },
   {
       "notification_id": "3",
       "flight_id": "6E 2343",
       "message": "Your flight 6E 2343 has been cancelled.",
       "timestamp": "2024-07-26T11:00:00Z",
       "method": "App",
       "recipient": "user_app_id_12345"
   }
]
collection2.insert_many(notification_data)
print("Notification data inserted successfully!")
client.close()
