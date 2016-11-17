FROM python:latest
RUN apt-get update

RUN mkdir /app
VOLUME /app
WORKDIR /app

RUN pip install botogram

CMD python /app/bot.py
