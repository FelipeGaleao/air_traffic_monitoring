import pika
import pandas as pd
import sys
sys.path.append('.')


from adapters.delta_rs import DeltaRSAdapter
from adapters.rabbit_mq import RabbitMQAdapter
import json
import sys


def consume_data():
    connection_url = "amqp://guest:guest@localhost:5672"
    connection = pika.BlockingConnection(pika.URLParameters(connection_url))
    rabbit_mq = RabbitMQAdapter(connection)
    method, properties, body = rabbit_mq.consume_from_queue("aircraft")
    if method is not None:
        write_file(body)
    else:
        return None


def write_file(data):
    data_json = json.loads(data)
    df = pd.DataFrame(data_json, dtype=str)
    columns = ['hex', 'type', 'flight', 'alt_baro', 'gs', 'track', 'squawk', 'nav_qnh', 'lat', 'lon', 'emergency']
    df = df[columns]
    df['airline'] = df['flight'].str[:3]
    delta_rs = DeltaRSAdapter()
    delta_rs.write_to_deltalake(df, "append")

if __name__ == "__main__":
    while True:
        consume_data()
