from celery import shared_task
from celery.exceptions import Reject



@shared_task(bind=True, autoretry_for=(ConnectionError,), retry_backoff=True, retry_kwargs={"max_retries": 3})
def process_orders(self, order_id: int) -> dict[str, object]:
    print(f"Processing your order: {order_id}")
    
    return {
        "order_id": order_id,
        "status":"completed"
    }
    
    
@shared_task(bind=True)
def failling_order(self, order_id: int) -> None:
    print(f"Processing order {order_id}")
    
    raise RuntimeError("Intentional order processing failure")


@shared_task(bind=True, acks_late=True)
def reject_order(self, order_id: int) -> None:
    print(f"Processing order {order_id}")
    
    raise Reject(
        "Intentional order processing failure",
        requeue=False
    )