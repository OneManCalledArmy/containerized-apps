from flask import Flask
import redis
import os

REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
app = Flask(__name__)


@app.route('/size')
def get_size():
    return f"{redis_client.dbsize()}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)