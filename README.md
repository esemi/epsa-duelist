# epsa-duelist

Simple telegram bot for to calculate the opponent's moves in telegram's MMORPG

## Local instalation 

```bash
$ git clone https://github.com/esemi/epsa-duelist.git
$ cd epsa-duelist/app
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -U poetry pip setuptools
$ poetry config virtualenvs.create false --local
$ poetry install
```

Create env file to override default config

```bash
cat > .env << EOF
throttling_time=2.0
debug=true
telegram_token=U_TELEGRAM_TOKEN
EOF
```

## Run test

```python
$ pytest --cov=app
```

## Run linters

```bash
$ poetry run mypy app/
$ poetry run flake8 app/
```

## Run background task

```python
python -m app.rates_update_task
```

## Run telegram bot

```python
python -m app.bot_app
```
