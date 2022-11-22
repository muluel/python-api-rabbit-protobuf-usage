#!/usr/bin/env python
import pika
import postSchema_pb2 as pb


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

post = pb.PostList.Post()

def callback(ch, method, properties, body):
    post.ParseFromString(body)
    print(" [x] Received %r" % post.name)
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()