FROM python:3.11-slim

WORKDIR /usr/src

COPY ./app .

RUN pip install -r requirements.txt

CMD [ "python", "./run.py" ]

