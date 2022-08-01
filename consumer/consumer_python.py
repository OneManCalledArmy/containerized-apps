# v1.0.1

import pika
import sys, os
import redis
from datetime import datetime

RABBIT_HOST = os.getenv('RABBIT_HOST')
RABBIT_PORT = os.getenv('RABBIT_PORT')
RABBIT_USERNAME=os.getenv('RABBIT_USERNAME')
RABBIT_PASSWORD=os.getenv('RABBIT_PASSWORD')
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)


def time_pid():
    pid = os.getpid()
    current_time = datetime.now()
    date_time = current_time.strftime("%Y/%m/%d/%H:%M:%S")
    output = date_time + '/' + str(pid)
    return output

def main():
    credentials = pika.PlainCredentials(RABBIT_USERNAME, RABBIT_PASSWORD)
    parameters = pika.ConnectionParameters(host=RABBIT_HOST, port=RABBIT_PORT, credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='q1')
    
    
    def callback(ch, method, properties, body):        
        redkey = time_pid()
        redis_client.set(redkey, body.decode())
        redis_client.expire(redkey, 60)

    
    channel.basic_consume(queue='q1', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)