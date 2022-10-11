# Xeneta's rates task

I have used flask, python-dateutil, psycopg-binary, python-dotenv libraries in this project.

## Initial Setup Requirements

I have used psql to import the database dump into rates database using this command:

```bash
psql -U postgres -d rates -1 -f rates.sql
```
## .env file

Create a .env file in the root directory of the project which stores database username and password. 

## Docker

If you want to run it in a docker container:

First build a container with:

```bash
docker build -t ratetask .
```

Then run:

```bash
docker run -p 5000:8080 ratetask
```

## Difficulties in the project

I had some difficulties during testing the app, because I have not done python API testing before.

## To run the project without docker

Run the command:

```bash
pip3 install -r requirements.txt
```
to install all the requirements for this project. Then run:

```bash
python app.py
```
to run the app.

## Thanks
I want to thank Xeneta for this opportunity, the task was fun and there are some areas where I can perform better.
