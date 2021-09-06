FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev && \
    python3 -m pip install --upgrade pip

COPY requirements.txt /

RUN python3 -m pip install -r requirements.txt

COPY . /recomender-system

WORKDIR /recomender-system

ADD . /recomender-system

ENTRYPOINT [ "python3" ]

EXPOSE 8000

CMD [ "main.py" ]