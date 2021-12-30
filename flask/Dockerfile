# basic python image
FROM python:3.10-slim

# declare the source directory
WORKDIR /usr/src/thisapp/flask
COPY requirements.txt .

RUN pip install -r requirements.txt

# Without this setting, Python never prints anything out.
ENV PYTHONUNBUFFERED=1

# copy the file
COPY app/ app/
COPY run.py .

# start commend
CMD ["python", "run.py"]