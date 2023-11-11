from celery import shared_task
from rabbitmq.producer import publish
@shared_task(name='rabbitmq.tasks.publish_message',
             bind=True,
             acks_late=True,
             autoretry_for=(Exception,),
             max_retries=5,
             retry_backoff=True,
             queue="read_write",
             retry_backoff_max=500,
             retry_jitter=True)
def publish_message(self, message):
    """
    celery `task` for sending messages 
    """
    publish(message)
    print(f"Message Published == {message}")
