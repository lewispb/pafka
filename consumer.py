from kafka import KafkaConsumer

topic = 'recipes'
group_id = 'pafka.recipes.v1'
consumer = KafkaConsumer(topic, group_id=group_id)

for msg in consumer:
    print (msg.headers)
    print (msg)
