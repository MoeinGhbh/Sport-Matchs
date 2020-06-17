# Sport API

## Project Report :

---

at first, the publisher read messages and edit format then send for the rabbitMQ queue.
second, consumer listens to queue when receive data pars them and save to SQLite.
I designed and implement normalization relational databases to save data.
I define a function to read customize data to JSON format for sending with restful API for ReactJS.
My ReactJS injected to the backend to when build project, send built file to the backend. 

### for run RabbitMQ need use docker image:

--- 

  * docker-compose up -d rabbitmq
  * http://localhost:15672 (username,password: guest,guest)


### Make ready enviroment, includes: install virtaul enviroment and install requierd library

---

  * python3 -m venv env

  * pip freeze > requirment.txt

  * pip instal pika
  * pip install sql_alchemy
  * pip install flask

### 

---

### make dabase from model modul:

---

  * python
  * from model import *
  * db.create_all()


### Run Publisher and consumer

---

  * cd consumer
  * python consumer.py
  * cd publisher
  * python publisher.py



### for run application

--- 

    python aap.py





## Require:

JSON formated messages are being published into a RabbitMQ queue (can be done manually on the RabbitMQ management UI).
Each one of the messages represents detailed information for an Sports API event and has a source referenced. Your task is to read them, save them (update if necessary) and provide the information for further use.

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



