FROM python

RUN apt update

RUN pip install poetry

#RUN cd /app && poetry install

RUN /home ls

WORKDIR /app

COPY . .

CMD echo “Hello World”
