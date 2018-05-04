FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y ubuntu-server python3-pip
RUN pip3 install --trusted-host pypi.python.org discord.py

RUN mkdir /app
WORKDIR /app
ADD . /app

CMD ["python3", "main.py"]