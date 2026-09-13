import os
from celery import Celery
from kombu import Exchange, Queue


os.environ.setdefault("DJANGO_SETTING_MODULE", "config.settings")

app = Celery("config")

app.config_from_object(
    "django.conf:settings",
    namespace="CELERY"
)


app.conf.task_queues = (
    Queue(
        "orders",
        Exchange("orders", type="direct"),
        routing_key="orders",
        durable=True,
        queue_arguments={
            "x-dead-letter-exchange": "orders.dlx",
            "x-dead-letter-routing-key": "orders.dlq",
        },
    ),
    Queue(
        "orders.dlq",
        Exchange("orders.dlx", type="direct"),
        routing_key="orders.dlq",
        durable=True,
    ),
)

app.conf.task_default_queue = "orders"
app.conf.task_default_exchange = "orders"
app.conf.task_default_routing_key = "orders"

app.autodiscover_tasks()