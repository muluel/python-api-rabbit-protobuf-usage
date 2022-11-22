#!/usr/bin/env python
import pika
import json
import postSchema_pb2 as pb
from google.protobuf.json_format import Parse


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

file = open('posts.json','r')
data = json.dumps(json.load(file))
file.close()

postList = Parse(data,pb.PostList())
print(type(postList))

for post in postList.posts:
    message = post.SerializeToString()
    channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ))
    print(" [x] Sent %r" % message)
connection.close()