FROM python:3.10

RUN mkdir /sender
WORKDIR /sender

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt requirements.txt

RUN  pip install --upgrade pip && pip install -r requirements.txt

COPY . .
COPY ./wait-for-it.sh /usr/bin/wait-for-it.sh
RUN chmod 777 /usr/bin/wait-for-it.sh
CMD ["wait-for-it.sh"]
