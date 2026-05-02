import json

from kafka import KafkaProducer


# create the kafka producer object for the datasets to use and send data to kafka itself
def create_kafka_producer(bootstrap_servers: str) -> KafkaProducer:
    """creates the kafka producer

    Args:
        bootstrap_servers (str): the url / name of the docker bootstrap server

    Returns:
        KafkaProducer: kafka producer connected to my kafka broker
    """
    return KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )


# this sends any 'local' data to the kafka broker / specific topic
def publish_records(producer: KafkaProducer, topic: str, records: list[dict]) -> None:
    """pushes records (data) to a topic

    Args:
        producer (KafkaProducer): kafka producer connected to my kafka broker
        topic (str): name of the topic to push records to
        records (list[dict]): the data to send to my kafka broker
    """
    for record in records:
        producer.send(topic, value=record)

    producer.flush()
