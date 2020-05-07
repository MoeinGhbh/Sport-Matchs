#!/usr/bin/env python
import pika
from model import Title, Team, Tournament , Matches
import json

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='eSportQueue')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    output_json = json.loads(body)
    
    # add title
    print('add title')
    print(output_json["data"]["title"],output_json["data"]["date_start_text"])
    Title.Insert(output_json["data"]["title"],output_json["data"]["state"])

    # add tournamte
    trnmt=""
    print('add tournamte',output_json["data"]["title"])
    tmp = output_json["data"]["tournament"]
    if len(tmp)==2:
        print(tmp["name"])
        Tournament.Insert(tmp["name"],output_json["data"]["title"],output_json["data"]["date_start_text"])
        trnmt = tmp["name"]
    else:
        print(output_json["data"]["tournament"])
        Tournament.Insert(output_json["data"]["tournament"],output_json["data"]["title"],output_json["data"]["date_start_text"])
        trnmt = output_json["data"]["tournament"]
    
    # add team
    print('add team')
    for tmp in output_json["data"]["teams"]:
        Team.Insert(tmp["id"],tmp["name"])
        print(tmp["id"],tmp["name"])

    # add Matches
    print('add matches')
    print(output_json["data"]["scores"][0]["team"])
    print(output_json["data"]["scores"][1]["team"])
    Matches.Insert(trnmt,output_json["data"]["scores"][0]["team"],output_json["data"]["scores"][1]["team"])


channel.basic_consume(queue='eSportQueue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()



