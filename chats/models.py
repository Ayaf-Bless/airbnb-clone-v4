from django.db import models
from core import models as core_models


class Chat(core_models.Core):
    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return " ".join(usernames)

    def count_messages(self):
        return self.messages.count()

    def count_participants(self):
        return self.participants.count()

class Message(core_models.Core):
    message = models.TextField()
    user = models.ForeignKey(to="users.User", on_delete=models.CASCADE, related_name="messages")
    chat = models.ForeignKey(to=Chat, on_delete=models.CASCADE, related_name="messages")

    def __str__(self):
        return f"{self.user} says... {self.message}"
