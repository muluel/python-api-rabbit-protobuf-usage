# python-api-rabbit-protobuf-usage
It wil shows how to use api requests and how to make message queue with it and how to use protocol buffer (a.k.a. protobuf)

## Usage:

After clone this repo.

cd python-api-rabbit-protobuf-usage

python -m venv venv

pip install -r requirements.txt


First thing you need to create env.py file and write your:
  - CLIENT_ID = 'Reddit app client_ID'
  - CLIENT_SECRET 'Reddit app client_secret'
  - USERNAME = 'Reddit_username'
  - PASSWORD = 'Reddit_password'


and run 

python getToken.py

it will prompt a token. Use that token for app.py

You can run app.py with arguments below

python app.py [token] [search_keyword] [post_count<=100]

## RabbitMQ server

If you don't have docker:
  You need to install docker first.

After basicly open a terminal and paste this command: 
```console
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management
```

Then just run 
  python worker.py
  python task.py