from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
import os
import json
import time
import requests


class KafkaUtility:
  def __init__(self, server, topic):
    self.__server = server
    self.__topic = topic

  def send_message_avro(self, message, schema_registry):
    value_schema = avro.loads(self.__get_latest_schema(schema_registry))
    avro_producer = AvroProducer({
      'bootstrap.servers': self.__server,
      'schema.registry.url': schema_registry
    }, default_value_schema=value_schema)
    avro_producer.produce(topic=self.__topic, value=message)
    avro_producer.flush()

  def __get_latest_schema(self, schema_registry, is_key=False):
    subject = self.__topic + ('-key' if is_key else '-value')
    r = requests.get(schema_registry + '/subjects/' + subject + '/versions')
    ver = json.loads(r.text)[-1]
    schema = requests.get(schema_registry + '/subjects/' + subject + '/versions/' + str(ver))
    return json.loads(schema.text)['schema']

if '__name__' == '__main__':
  print('hihih')
  # bootstrap_server = 'localhost:9092'
  # schema_registry = 'http://localhost:8081'
  # topic = 'df_file_uploaded_avro'
  # business_id = 130000001
  # node_group = 'd30.demandforced3.com'
  # file_path = 'abc.zip'
  #
  # kafka = KafkaUtility(bootstrap_server, topic)
  # message = {
  #   'publisher': 'test publisher',
  #   'businessId': business_id,
  #   'nodeGroup': node_group,
  #   'fileName': os.path.basename(file_path),
  #   'arrivalTime': time.time(),
  #   'uploadType': 'FULL',
  #   'fileSizeBytes': long(os.path.getsize(file_path))
  # }
  # kafka.send_message_avro(message, schema_registry)
