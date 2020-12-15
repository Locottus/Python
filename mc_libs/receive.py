#!/usr/bin/env python
import pika, sys, os

queue = 'hello'
routing_key = 'hello'
mq_host = 'localhost'


def receiveMessageToMQ():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host= mq_host))
    channel = connection.channel()
    channel.queue_declare(queue= queue)
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())
    channel.basic_consume(queue= queue, on_message_callback=callback, auto_ack=True)
    #print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()




if __name__ == '__main__':
#    try:
        receiveMessageToMQ()
'''
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

'''
