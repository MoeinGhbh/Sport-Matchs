#!/usr/bin/env python
import pika
from model import Matches, Title, Team, Tournament
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='eSportQueue')

def callback(ch, method, properties, body):
    # print(" [x] Received %r" % body)
    output_json = json.loads(body)
    
    # add title
    print('add title')
    print(output_json["data"]["title"],output_json["data"]["date_start_text"])
    Title.Insert(output_json["data"]["title"],output_json["data"]["date_start_text"],output_json["data"]["state"])

    # add team
    print('add team')
    for tmp in output_json["data"]["teams"]:
        Team.Insert(tmp["id"],tmp["name"])
        print(tmp["id"],tmp["name"])
        # Team.Insert(tmp["id"],tmp["name"])

    # add tournamte
    print('add tournamte')
    tmp = output_json["data"]["tournament"]
    if len(tmp)==2:
        print(tmp["name"])
        Tournament.Insert(tmp["name"])
    else:
        print(output_json["data"]["tournament"])
        Tournament.Insert(output_json["data"]["tournament"])

channel.basic_consume(queue='eSportQueue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()



