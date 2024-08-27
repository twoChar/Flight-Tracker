# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import pika
# import json
# import pymongo

# app = Flask(__name__)
# CORS(app)  # Enable CORS

# # MongoDB setup
# client = pymongo.MongoClient("mongodb://localhost:27017/")
# db = client["flight_data"]
# collection = db["flights"]

# def send_notification(notification):
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#     channel = connection.channel()
#     channel.queue_declare(queue='notifications')
#     channel.basic_publish(
#         exchange='',
#         routing_key='notifications',
#         body=json.dumps(notification)
#     )
#     connection.close()

# @app.route('/send_notification', methods=['POST'])
# def send_notification_route():
#     data = request.json
#     send_notification(data)
#     return jsonify({'status': 'Notification sent'}), 200

# @app.route('/flights', methods=['GET'])
# def get_flights():
#     flights = list(collection.find({}, {"_id": 0}))  # Exclude MongoDB's default "_id" field
#     return jsonify(flights)

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
import pika
import json
import pymongo
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS

# MongoDB setup
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["flight_data"]
flights_collection = db["flights"]
notifications_collection = db["notifications"]

def send_notification(notification):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='notifications')
    channel.basic_publish(
        exchange='',
        routing_key='notifications',
        body=json.dumps(notification)
    )
    connection.close()

@app.route('/send_notification', methods=['POST'])
def send_notification_route():
    data = request.json
    send_notification(data)
    return jsonify({'status': 'Notification sent'}), 200

@app.route('/flights', methods=['GET'])
def get_flights():
    flights = list(flights_collection.find({}, {"_id": 0}))  # Exclude MongoDB's default "_id" field
    return jsonify(flights)

@app.route('/notifications', methods=['GET'])
def get_notifications():
    notifications = list(notifications_collection.find({}, {"_id": 0}))  # Exclude MongoDB's default "_id" field
    return jsonify(notifications)

@app.route('/insert_flight_data', methods=['POST'])
def insert_flight_data():
    data = request.json
    if not isinstance(data, list):
        return jsonify({'error': 'Invalid data format. Expected a list of flight records.'}), 400
    try:
        # Convert string dates to datetime objects
        for record in data:
            if 'scheduled_departure' in record:
                record['scheduled_departure'] = datetime.fromisoformat(record['scheduled_departure'].replace('Z', '+00:00'))
            if 'scheduled_arrival' in record:
                record['scheduled_arrival'] = datetime.fromisoformat(record['scheduled_arrival'].replace('Z', '+00:00'))
            if 'actual_departure' in record and record['actual_departure']:
                record['actual_departure'] = datetime.fromisoformat(record['actual_departure'].replace('Z', '+00:00'))
            if 'actual_arrival' in record and record['actual_arrival']:
                record['actual_arrival'] = datetime.fromisoformat(record['actual_arrival'].replace('Z', '+00:00'))
        
        # Insert flight data into MongoDB
        flights_collection.insert_many(data)
        return jsonify({'status': 'Flight data inserted successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/insert_notification_data', methods=['POST'])
def insert_notification_data():
    data = request.json
    if not isinstance(data, list):
        return jsonify({'error': 'Invalid data format. Expected a list of notification records.'}), 400
    try:
        # Convert string dates to datetime objects
        for record in data:
            if 'timestamp' in record:
                record['timestamp'] = datetime.fromisoformat(record['timestamp'].replace('Z', '+00:00'))

        # Insert notification data into MongoDB
        notifications_collection.insert_many(data)
        return jsonify({'status': 'Notification data inserted successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
