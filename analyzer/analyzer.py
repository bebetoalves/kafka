import os
import json
from collections import deque
from time import sleep
import time
from confluent_kafka import Consumer, Producer
from loguru import logger

if __name__ == "__main__":
    bootstrap_servers = os.environ.get("KAFKA_BROKER")
    consumer = Consumer(
        {
            "bootstrap.servers": bootstrap_servers,
            "group.id": "analyzer",
            "auto.offset.reset": "earliest",
        }
    )
    producer = Producer({"bootstrap.servers": bootstrap_servers})
    message_queue = deque(maxlen=5)

    consumer.subscribe(["heat", "humidity"])

    while True:
        message = consumer.poll(1.0)

        if message is None:
            continue

        if message.error():
            logger.error(message.error())
            continue

        value = json.loads(message.value().decode("utf-8"))
        value = value["value"]

        message_queue.append(value)

        if len(message_queue) == message_queue.maxlen:
            min_value = min(message_queue)
            max_value = max(message_queue)
            avg_value = sum(message_queue) / len(message_queue)

            result = {
                "min": min_value,
                "max": max_value,
                "avg": avg_value,
                "timestamp": int(time.time()),
            }

            logger.info(result)

            producer.produce("analysis", value=json.dumps(result).encode("utf-8"))
            producer.flush()

        sleep(1)
