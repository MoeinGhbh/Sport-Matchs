#!/usr/bin/env python
import pika
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='eSportQueue')

for i in range(1,5):
    FileName = 'Messages/message{}.json'.format(i)

    with open(FileName,'r') as f:
        s = f.read()
        s = s.replace('\t','')
        s = s.replace('\n','')
        s=s.replace(' ','')
        s = s.replace(',}','}')
        s = s.replace(',]',']')
        data = json.loads(s)
        data = json.dumps(data)

    channel.basic_publish(exchange='', routing_key='eSportQueue', body=data)
    
print(" [x] Sent 'Messages sent'")
connection.close()




