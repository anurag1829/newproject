from kafka import KafkaProducer
import json

def send_to_kafka(topic, data):
    producer = KafkaProducer(
        bootstrap_servers=['your_kafka_broker:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    
    producer.send(topic, data)
    producer.flush()
    print(f"Data sent to Kafka topic {topic}")

if __name__ == "__main__":
    topic = 'your_topic'
    data = {'key': 'value'}  # Replace with your actual data
    
    send_to_kafka(topic, data)

