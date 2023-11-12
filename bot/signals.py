from django.db.models.signals import post_save
from django.dispatch import receiver

from bot.utils import start_chat
from .models import Chat,Message
@receiver(post_save,sender=Message)
def send_message_to_server(sender, instance, created, **kwargs):
    print("run send_message_to_server *signal*")
    start_chat(user_info= {
        "vegetarian":"yes",
        "vegan":"no",
        "gluten_free":"no",
        "dairy_free":"no",
        "nut_allergy":"no",
        "age":40,
        "calories_goal":4000,
        "weight":80,
    } 
    ,chat_id="test"
    )   
 