FROM python:3.10-slim

ARG RUN_ID

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD echo "Downloading model with RUN_ID=$RUN_ID"