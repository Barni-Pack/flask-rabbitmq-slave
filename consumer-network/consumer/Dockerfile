# basic python image
FROM python:3.10-slim

# install pika to access rabbitmq
RUN pip install pika

# Without this setting, Python never prints anything out.
ENV PYTHONUNBUFFERED=1

# declare the source directory
WORKDIR /usr/src/thisapp/consumer

# copy the file
COPY consumer.py .

# start commend
CMD ["python", "consumer.py"]