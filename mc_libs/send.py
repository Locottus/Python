#!/usr/bin/env python
import pika

queue = 'hello'
routing_key = 'hello'
mq_host = 'localhost'



def sendMessageToMQ(body):
    print('sending to mq',body)
    connection = pika.BlockingConnection( pika.ConnectionParameters(host= mq_host ))
    channel = connection.channel()
    channel.queue_declare(queue= queue)
    channel.basic_publish(exchange='', routing_key= routing_key , body= str(body))
    #print(" [x] Sent 'Hello World !'")
    connection.close()


for x in range(1, 12):
    sendMessageToMQ(x)
