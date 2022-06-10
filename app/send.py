#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
body_message = 'Hello World!'

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=body_message)

channel.basic_publish(exchange='', routing_key='hello', body=body_message)
print(" [x] Sent 'Hello World!'")
connection.close()
