docker-compose up -d rabbitmq

http://localhost:15672 (username,password: guest,guest)

python3 -m venv env
pip instal pika
pip install sql_alchemy
pip install flask


# make data base by model

---

  * python
  * from model import *
  * db.create_all()



python consumer.py
python publisher.py


# Intro

JSON formated messages are being published into a RabbitMQ queue (can be done manually on the RabbitMQ management UI).
Each one of the messages represents detailed information for an eSports event and has a source referenced. Your task is to read them, save them (update if necessary) and provide the information for further use.

Do not change the content of the message JSONs, since their content is intended to be as they are and they must be consumed in order.

# Features
* Run RabbitMQ in a docker container (with a docker-compose configuration)
* Publish and consume messages with the Python package `pika`
* Consumed messages are stored in a database in models like:
  * Title
  * Tournament
  * Team
  * Match
  * Scores of a Team in a Match
* Expose the data either on a API or `Website`
  * List all matches with teams (and scores) and filter by `title`, `tournament`, `state`, `date_start__gte`and `date_start_lte`
  * Detail view of a match

# Bonus
* Handle RabbitMQ exceptions (disconnect, service unreachable, etc.)
* Add logging through Python's `logging`
* Serve API data through ElasticSearch (service description in docker-compose.yml)
* Try to merge similiar items together - propose a way to connect them together

Aim for compleating the flow of information from recieving it to exposing it. We value your time, so choose to do some of the bonus features if you have time and take the ones you are most experienced and familiar with.

Give yourself four to six hours to complete the challenge. As a result we expect a docker-compose configuration to run the backend, consumer and RabbitMQ and your code as link to a repo on github or bitbucket with a README. Describe your choices and decisions in a few words.

Preferred usage of Python packages:
- django
- django-restframework
- flask
- flask-restful
- pika
- elasticsearch-dsl
- django-elasticsearch-dsl
- django-elasticsearch-dsl-drf
