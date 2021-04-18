FROM python:alpine3.12

WORKDIR /posts-analyzer

ADD . /posts-ananlyzer

RUN pip3 install -r requirements.txt


CMD [ "python", "main.py" ]