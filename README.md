# django-celery-dlq

A small Django + Celery demo showing how to route failed tasks to a dead letter queue (DLQ) on RabbitMQ.

## Stack

- Django 5
- Celery 5 + RabbitMQ
- Flower (task monitoring)
- django-celery-results

## Queues

- `orders` — default work queue. Configured with a dead-letter exchange `orders.dlx` and routing key `orders.dlq`.
- `orders.dlq` — dead letter queue that receives rejected/failed messages.

Tasks in `app/tasks.py`:

- `process_orders` — succeeds, auto-retries on `ConnectionError`.
- `failling_order` — raises `RuntimeError`; the message is rejected and lands in the DLQ.
- `reject_order` — explicitly rejects without requeue.

## Run with Docker

```bash
docker compose up --build
```

- Django: http://localhost:8000
- Flower: http://localhost:5555
- RabbitMQ management: http://localhost:15672 (`appuser` / `apppassword`)

## Run locally

Start RabbitMQ, then:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

In separate terminals:

```bash
celery -A config worker -l INFO
celery -A config flower --port=5555
```

## Endpoints

- `/admin/`
- `/api/test/` — prints students and teachers, returns them.
