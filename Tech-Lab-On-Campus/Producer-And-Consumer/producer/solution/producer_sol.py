import pika
import os

class mqProducer(myProducerInterface):
    def __init__(self, routing_key: str, exchange_name: str) -> None:
    # Save parameters to class variables
        self.routing_key = routing_key
        self.exchange_name = exchange_name
    # Call setupRMQConnection
        self.setupRMQConnection()

        pass

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters=con_params)       
        # Establish Channel
        self.channel = self.connection.channel()    
        # Create the exchange if not already present
        self.exchange = self.channel.exchange_declare(exchange="Exchange Name")
        pass

    def publishOrder(self, message: str) -> None:
        
        # Basic Publish to Exchange
        self.channel.basic_publish(
            exchange="Exchange Name",
            routing_key="Routing Key",
            body=message,
        )

        # Close Channel and Close Connection
        self.channel.close()
        self.connection.close()      
        pass
