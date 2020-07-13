import redis

import os
from flask import Flask


app = Flask(__name__)
redis = redis.StrictRedis(host=os.environ.get('REDIS_HOST'),
			  port=os.environ.get('REDIS_PORT'),
			  db=os.environ.get('REDIS_DB'),
			  password=os.environ.et('REDIS_PASSWORD')


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/visitor')
def visitor():
    redis.incr('visitor')
    visitor_num = redis.get('visitor').decode("utf-8")
    return "Visitor: %s" % (visitor_num)


@app.route('/visitor/reset')
def reset_visitor():
    redis.set('visitor', 0)
    visitor_num = redis.get('visitor').decode("utf-8")
    return "Visitor is reset to %s" % (visitor_num)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
