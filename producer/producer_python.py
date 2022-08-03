#v1.0.5 - connection not failing

from flask import Flask, request
import pika
import os

RABBIT_HOST = os.getenv('RABBIT_HOST')
RABBIT_PORT = os.getenv('RABBIT_PORT')
RABBIT_USERNAME=os.getenv('RABBIT_USERNAME')
RABBIT_PASSWORD=os.getenv('RABBIT_PASSWORD')

app = Flask(__name__)

credentials = pika.PlainCredentials(RABBIT_USERNAME, RABBIT_PASSWORD)
parameters = pika.ConnectionParameters(host=RABBIT_HOST, port=RABBIT_PORT, credentials=credentials)
connection = pika.BlockingConnection(parameters)


@app.route('/health')
def health():
    return f"200"

@app.route('/add', methods = ['POST'])
def process():
    if request.method == 'POST':        
        data = request.json
        channel = connection.channel()
        channel.queue_declare(queue='q1')
        channel.basic_publish(exchange='', routing_key='q1', body=str(data))
        return 'Done'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
