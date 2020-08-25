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
            "bootstrap.servers": self.__server,
            "schema.registry.url": schema_registry
        }, default_value_schema=value_schema)
        avro_producer.produce(topic=self.__topic, value=message)
        avro_producer.flush()

    def __get_latest_schema(self, schema_registry, is_key=False):
        subject = self.__topic + ("-key" if is_key else "-value")
        r = requests.get(schema_registry + "/subjects/" + subject + "/versions")
        ver = json.loads(r.text)[-1]
        schema = requests.get(schema_registry + "/subjects/" + subject + "/versions/" + str(ver))
        return json.loads(schema.text)["schema"]

if __name__ == "__main__":

    print "Start"
    #95F59D26-DBEE-9B78-D346-928806A2381E
    bootstrap_server = "localhost:9092"
    schema_registry = "http://localhost:8081"
    topic = "df_file_uploaded_avro"
    business_id = "130000001"
    node_group = "d30.demandforced3.com"
    file_path = r"D:\INTG\130000001.ng30D1_Full.2019-05-04-14-33-33\130000001.ng30D1_Full.2019-05-04-14-33-33.zip"

    kafka = KafkaUtility(bootstrap_server, topic)
    message = {
        "publisher": "dflink_services",
        "businessId": business_id,
        "nodeGroup": node_group,
        "fileName": os.path.basename(file_path),
        "arrivalTime": long(time.time()),
        "uploadType": "full",
        "fileSizeBytes": long(os.path.getsize(file_path))
    }
    print message
#     print """{"publisher": "dflink_services", "businessId": "130000001", "nodeGroup": "d30.demandforced3.com", "fileName": "130000001.d30.2019-05-23-01-48-36.zip", "arrivalTime": 1558601316, "uploadType": "UNKNOWN", "fileSizeBytes": 2359})
# """
    kafka.send_message_avro(message, schema_registry)
    print 'End'
