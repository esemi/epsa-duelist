# epsa-duelist
TODO badges

Telegram bot for calculating the opponent's move probability in the online game The Epsilion Wars.

[Bot (staging)](https://t.me/rty_betabot)

## Local installation

```bash
$ git clone https://github.com/esemi/epsa-duelist.git
$ cd epsa-duelist
$ python3.11 -m venv venv
$ source venv/bin/activate
$ pip install -U poetry pip setuptools
$ poetry install
```

Create env file to override default config
```bash
cat > .env << EOF
telegram_token=U_TELEGRAM_TOKEN
EOF
```

## Run test

```bash
$ pytest --cov=app
```

## Run linters

```bash
$ poetry run mypy app/
$ poetry run flake8 app/
```

## Run telegram bot

```bash
$ python -m app.bot
```