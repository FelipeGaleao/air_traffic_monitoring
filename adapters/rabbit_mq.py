class RabbitMQAdapter:
    def __init__(self, connection):
        self.connection = connection

    def publish_to_queue(self, queue_name, message):
        self.connection.channel().basic_publish(exchange='', routing_key=queue_name, body=message)

    def process_message(self, ch, method, properties, body):
        return ch, method, properties, body

    def consume_from_queue(self, queue_name):
       method, properties, body = self.connection.channel().basic_get(queue=queue_name, auto_ack=True)
       return method, properties, body

    def create_queue(self, queue_name):
        self.connection.channel().queue_declare(queue=queue_name)

    def get_queues(self):
        # list queues 
        queues = self.connection.channel().queue_declare(queue='', passive=True)
        return queues
