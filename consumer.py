import json
import importlib
import stringcase
from kafka import KafkaConsumer

topic = 'recipes'
group_id = 'pafka.recipes.v1'
consumer = KafkaConsumer(topic, group_id=group_id, value_deserializer=json.loads)

for msg in consumer:
    # import pdb; pdb.set_trace()
    class_name = stringcase.pascalcase(msg.value['type'])
    HandlerClass = getattr(importlib.import_module('handlers'), class_name)
    HandlerClass(msg).run()
