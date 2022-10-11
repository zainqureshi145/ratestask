FROM postgres:12
FROM python:3

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB rates

COPY rates.sql /docker-entrypoint-initdb.d/

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

ENV PORT=8080

EXPOSE 8080


CMD ["python", "app.py"]