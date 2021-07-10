FROM python:3.8.3-alpine
# ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add build-base libffi-dev openssl-dev postgresql-dev zlib-dev jpeg-dev gcc musl-dev --no-cache


RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./docker-entrypoint.sh .

# copy project
COPY . .
RUN chmod +x docker-entrypoint.sh
# run entrypoint.sh
ENTRYPOINT ["/usr/src/backend/docker-entrypoint.sh"]
