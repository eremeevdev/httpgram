FROM python:latest
RUN apt-get update

RUN mkdir /app
VOLUME /app
WORKDIR /app

RUN pip install botogram
RUN pip install pymongo

CMD python /app/bot.py
