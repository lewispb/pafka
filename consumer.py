import json
import importlib
import stringcase
from kafka import KafkaConsumer

# Kafka
TOPIC = 'recipes'
GROUP_ID = 'pafka.recipes.v1'
CONSUMER = KafkaConsumer(TOPIC, group_id=GROUP_ID, value_deserializer=json.loads)

for msg in CONSUMER:
    # import pdb; pdb.set_trace()
    class_name = stringcase.pascalcase(msg.value['type'])
    HandlerClass = getattr(importlib.import_module('handlers'), class_name)
    HandlerClass(msg).run()
