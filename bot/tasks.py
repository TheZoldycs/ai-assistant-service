from celery import shared_task
from rabbitmq.tasks import publish_message

@shared_task(
        name="bot.tasks.send_reply_to_base_server"
)
def send_reply_to_base_server(self,reply):
    """
    `celery` task to send Ai reply to base server via ::amqp protocol
    """
    reply_json = {"reply":reply}
    publish_message.delay(reply_json)