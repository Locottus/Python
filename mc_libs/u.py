
#!/usr/bin/env python
import pika, sys, os

queue = 'HealthJump'
routing_key = ''
mq_host = '3.235.107.32'





x = {'current_page': 1, 'data': [], 'from': None, 'last_page': 0, 'next_page_url': None, 'path': 'https://api.healthjump.com/hjdw/SBOX02/payer_dim', 'per_page': 1000, 'prev_page_url': None, 'to': None, 'total': 0}


RABBIT_HOST = '3.235.107.32'#os.environ['RABBIT_HOST']
RABBIT_USER = 'admin'#os.environ['RABBIT_USER']
RABBIT_PWD = 'RQDpTAKGh8eD88fh'#os.environ['RABBIT_PWD']
credentials = pika.PlainCredentials(RABBIT_USER, RABBIT_PWD)
parameters = pika.ConnectionParameters(credentials=credentials, host=RABBIT_HOST)


def receiveMessageToMQ():
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    #channel.queue_declare(queue= queue)
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())
    channel.basic_consume(queue= queue, on_message_callback=callback, auto_ack=True)
    #print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()




if __name__ == '__main__':
    try:
        receiveMessageToMQ()

    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


