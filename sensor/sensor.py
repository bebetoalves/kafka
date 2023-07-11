import os
import json
from confluent_kafka import Producer
from time import sleep
import random
import time
from loguru import logger
import threading


class Sensor:
    def __init__(self, name: str, min: int, max: int) -> None:
        self.name = name
        self.min = min
        self.max = max
        bootstrap_servers = os.environ.get("KAFKA_BROKER")
        self.producer = Producer({"bootstrap.servers": bootstrap_servers})

    def produce(self) -> None:
        while True:
            data = {
                "value": random.uniform(self.min, self.max),
                "timestamp": int(time.time()),
            }

            logger.info("{} - {}".format(self.name, data))

            self.producer.produce(self.name, value=json.dumps(data).encode("utf-8"))
            self.producer.flush()

            sleep(1)


if __name__ == "__main__":
    heat = Sensor("heat", 20, 30)
    humidity = Sensor("humidity", 40, 60)

    heat_thread = threading.Thread(target=heat.produce)
    humidity_thread = threading.Thread(target=humidity.produce)

    heat_thread.start()
    humidity_thread.start()

    heat_thread.join()
    humidity_thread.join()
