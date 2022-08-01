# tester:v1.0.0

from flask import Flask
import os

TEST_KEY = os.getenv('test-key')

app = Flask(__name__)

@app.route('/health')
def health():
    return f"200"


@app.route('/size')
def get_size():
    return TEST_KEY


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
