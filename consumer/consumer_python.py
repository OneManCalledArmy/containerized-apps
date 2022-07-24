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


# pid = os.getpid()
# now = datetime.now()
# date_time = now.strftime("%Y/%m/%d/%H:%M:%S")

def main():
    credentials = pika.PlainCredentials(RABBIT_USERNAME, RABBIT_PASSWORD)
    parameters = pika.ConnectionParameters(host=RABBIT_HOST, port=RABBIT_PORT, credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='q1')
    
    idx = 0
    
    def callback(ch, method, properties, body):
        nonlocal idx
        
        redis_client.set(idx, body.decode())
        redis_client.expire(idx, 60)
        idx += 1
    
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