import pika
import json

def callback(ch, method, properties, body):
    notification = json.loads(body)
    print(f" [x] Received {notification}")
    # Process the notification (e.g., send SMS, email, or app notification)

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='notifications')

# Set up subscription on the queue
channel.basic_consume(queue='notifications', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
