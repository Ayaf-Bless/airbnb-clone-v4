from django.db import models
from core import models as core_models


class Chat(core_models.Core):
    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return str(self.created_at)


class Message(core_models.Core):
    message = models.TextField()
    user = models.ForeignKey(to="users.User", on_delete=models.CASCADE)
    chat = models.ForeignKey(to=Chat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says... {self.message}"
