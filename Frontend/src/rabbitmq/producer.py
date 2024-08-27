import pika
import json

def send_notification(notification):
    # Connect to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue='notifications')

    # Publish the notification to the queue
    channel.basic_publish(
        exchange='',
        routing_key='notifications',
        body=json.dumps(notification)
    )

    print(f" [x] Sent {notification}")
    connection.close()

notifications = [
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

for notification in notifications:
    send_notification(notification)
