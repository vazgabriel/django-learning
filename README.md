# Django Learning

Django project while learning

## Running

First, you will need to install [Docker](https://www.docker.com/)
Then Just run

```bash
docker-compose up
```

### Install (Without Docker)

In this case you may want to install some database and change the information on settings.py

```bash
# Create venv
python3 -m venv ./venv

# Activate (MAC / Linux)
source ./venv/bin/activate
# Activate (Windows)
venv\Scripts\activate

# Then install
pip install -r requirements.txt
```

To deactivate venv just run

```bash
deactivate
```

### Run (Without Docker)

```bash
python3 manage.py run-server
```
