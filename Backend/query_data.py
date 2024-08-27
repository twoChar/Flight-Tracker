import pymongo

# Establish a connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create or switch to the 'flight_data' database
db = client["flight_data"]

# Create or switch to the 'flights' collection
collection = db["flights"]

# Retrieve all flight documents
all_flights = collection.find()

for flight in all_flights:
    print(flight)
