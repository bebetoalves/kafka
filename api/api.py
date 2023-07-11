import json
import os
from flask import Flask, jsonify
from flask_socketio import SocketIO
from confluent_kafka import Consumer
from threading import Thread
from loguru import logger


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
socketio = SocketIO(app, cors_allowed_origins="*")


def kafka_consumer():
    consumer = Consumer(
        {
            "bootstrap.servers": os.environ.get("KAFKA_BROKER"),
            "group.id": "api",
            "auto.offset.reset": "earliest",
        }
    )

    consumer.subscribe(["heat", "humidity", "analysis"])

    while True:
        message = consumer.poll(1.0)

        if message is None:
            continue

        if message.error():
            logger.error(message.error())
            continue

        socketio.emit(
            "push", {"name": message.topic(), **json.loads(message.value().decode())}
        )


@socketio.on("connect")
def handle_connect():
    kafka_thread = Thread(target=kafka_consumer)
    kafka_thread.start()


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=8000, allow_unsafe_werkzeug=True)
