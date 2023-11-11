from bot.tasks import send_message_to_ai_assistant
from rabbitmq.consumer import Consume
import json
from datetime import datetime

colors = {
    "yellow": "\033[1;33m",
    "green": "\033[1;32m",
    "cyan": "\033[1;36m",
    "red": "\033[1;31m",
    "white": "\033[1;37m"
}
class MessageProcessing(Consume):
    """A class for processing messages from `RabbitMQ`"""

    def default_callback(self, ch, method, proterties, body):
        """
        Default callback for processing messages from RabbitMQ.
        Loads the message body as JSON, prints it, and acknowledges the message.
        """
        now = datetime.now()
        print(f"{colors['white']}\n{now} New message ==> {json.loads(body)}\033[0m")
        message = json.loads(body.decode("utf-8"))
        print(message)
        # Do whatever you want with messages here
        sender = message.get("sender")
        model = message.get("model")
        receiver = message.get("receiver")
        data = message.get("data")
        if sender == "BASE_SERVER" and receiver == "AI_SERVICE":
            print("sender == BASE_SERVER and receiver == AI is true")
            if model == "Chat":
                print("Run send_message_to_ai_assistant task ..........")
                send_message_to_ai_assistant.delay(data=data)
        # This line is important to consume messages and do not receive them again
        ch.basic_ack(delivery_tag=method.delivery_tag)
    def __init__(self, callback=None):
        """
        Initialize the MessageProcessing class.
        If no callback is provided, the default_callback method is used.
        """
        if not callback:
            callback = self.default_callback
        super().__init__(callback)
