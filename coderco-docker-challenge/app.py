from flask import Flask
import redis

app = Flask(__name__)

redis_client = redis.Redis(host="redis", port=6379)


@app.route("/")
def home():
    return "Welcome to my Docker challenge"

@app.route("/count")
def visits():
    count = redis_client.incr("visits")
    return f"Visit count: {count}"
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)