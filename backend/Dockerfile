FROM python:3.4.5-slim
WORKDIR /code

# ENV FLASK_APP=main.py
# ENV FLASK_RUN_HOST 0.0.0.0

# ENV PYTHONPATH "/usr/src/app/:/usr/src/app/modules/"

ENV PATH=$PATH:/consumer
ENV PYTHONPATH /consumer


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3","app.py","--host","0.0.0.0"]