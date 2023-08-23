# Sumeet Backend
***
# Local development
## Initial requirements

With default configs project requires:
 - `postgres` running on default `5432` localhost port with
    `POSTGRES_PASSWORD=postgres_password` `POSTGRES_USER=postgres` for project itself.

Project uses `venv` for dependency management:
```shell
python3 -m venv venv
```

activate venv :
```shell
venv/bin/activate
```

requirements :
```shell
pip install -r requirements.txt
```

Copy and configure `.env.prod` file.
```shell
cp .env.example .env.prod
```

## Running Localhost

Run server:
```shell
python3 manage.py runserver
```

Run worker:
```shell
celery -A sumeet_backend worker -l INFO
```

Run bot:
```shell
python3 manage.py bot
```

***

# Production deployment

Project was dockerized with love.

## Initial requirements

* docker
* docker compose

### Manual deployment

1. Copy and configure `.env.prod` file.
```shell
.env.example .env.prod
```
2. Run docker-compose
```shell
docker-compose up --build
```


