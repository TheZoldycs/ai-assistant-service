from django.db import models

# Create your models here.


class Chat(models.Model):
    client_chat_id = models.CharField(("Id"), max_length=150)
    def __str__(self):
        return self.client_chat_id
    


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    reply = models.TextField(("reply"))
    
