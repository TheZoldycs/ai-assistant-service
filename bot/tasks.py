from celery import shared_task
from rabbitmq.tasks import publish_message
from .assistant import start_chat
from bot.models import Chat,Message

@shared_task(
        name="bot.tasks.send_reply_to_base_server"
)
def send_reply_to_base_server(self,reply):
    """
    `celery` task to send Ai reply to base server via ::amqp protocol
    """
    reply_json = {"reply":reply}
    publish_message.delay(reply_json)


@shared_task(
    name="bot.tasks.send_message_to_ai_assistant"
)
def send_message_to_ai_assistant(self,data):
    """
    `celery` task to send message to ai assistant service
    """
    chat_id=data.get("chat_id")
    message=data.get("message")
    user_info=data.get("user_info")
    #get or create chat 
    chat,created = Chat.objects.get_or_create(id=chat_id)
    # create message after that we need to create a signal for send it to base server client
    Message.objects.create(
        chat=chat,message=message
    )
    #execute function
    start_chat(user_info=user_info,chat_id=chat_id)

