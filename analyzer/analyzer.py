from typing import List
from confluent_kafka import Consumer, Producer
import json

def analyze_sensor_data(data: List[str]) -> dict:
    # Este método é responsável por tratar os dados que estão no tópico do Kafka.
    # A mensagem chegará dessa forma: ['{"nome": "Sensor X", "leitura": 0}', '{"nome": "Sensor Y", "leitura": 1}']
    # Você então deverá fazer um "parse" dessas mensagens e criar uma nova mensagem.
    # O formato da nova mensagem deverá ser, por exemplo: {"min": 0, "max": 1, "media": "0.5"}

def delivery_report(err, msg) -> None:
    # Este método deverá ser usado para imprimir se houve erro no envio da mensagem ou sucesso (exibir a mensagem enviada).

def process_sensor_data() -> None:
    # Este método fará duas operações: Consumir e Produzir.
    # Ele irá consumir as mensagens geradas pelo sensor (use o método analyze_sensor_data() para tratar essas mensagens).
    # Ele também irá produzir mensagens com a análise feita, use o tópico "analises".
    # Use como callback do Producer o método delivery_report()

process_sensor_data()
