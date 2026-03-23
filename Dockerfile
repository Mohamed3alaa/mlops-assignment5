FROM python:3.10-slim

# argument
ARG RUN_ID

# set working directory
WORKDIR /app

# copy files
COPY . .

# install dependencies
RUN pip install -r requirements.txt

# mock download model
CMD echo "Downloading model with RUN_ID=$RUN_ID"