import json
import requests
import time
import sys 
sys.path.append('.')
from adapters.rabbit_mq import RabbitMQAdapter
import pika

connection_url = "amqp://guest:guest@localhost:5672"
connection = pika.BlockingConnection(pika.URLParameters(connection_url))
rabbit_mq = RabbitMQAdapter(connection)


def capture_data():
    url = "https://tar1090.trafegoaereo.com.br/tar1090/data/aircraft.json"
    response = requests.get(url)
    data = json.loads(response.text)['aircraft']
    return data

def publish_data(data):

    data_encoded = json.dumps(data)
    rabbit_mq.publish_to_queue("aircraft", data_encoded)
    print("Data published to queue")

def create_queue():
    rabbit_mq.create_queue("aircraft")
    print("Queue created")

if __name__ == "__main__":
    # check if the queue exists
    rabbit_mq.create_queue("aircraft")
    while True:
        data = capture_data()
        publish_data(data)
        time.sleep(1)