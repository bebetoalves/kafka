from confluent_kafka import Producer
import json

def generate_sensor_data() -> dict:
    # Este método é responsável por gerar dados aleatórios de sensores.
    # Formato esperado: {"sensor": "nome do sensor", "leitura": "leitura do sensor"}.

def delivery_report(err, msg) -> None:
    # Este método deverá ser usado para imprimir se houve erro no envio da mensagem ou sucesso (exibir a mensagem enviada).

def produce_sensor_data() -> None:
    # Esse método deverá ser usado para "produzir" os dados.
    # Ele irá se conectar ao servidor através da porta 9092, vai gerar dados através do generate_sensor_data()
    # E enviará para o tópico "sensores"
    # Use como callback o método delivery_report()

produce_sensor_data()
