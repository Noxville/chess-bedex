FROM ubuntu:20.10
RUN apt-get update && apt-get -y install apt-utils stockfish python3 python3-pip
RUN pip3 install chess
COPY ./src /app
CMD ["/usr/bin/python3", "-u", "/app/play.py"]
