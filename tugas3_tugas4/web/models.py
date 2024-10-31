from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    login_count = models.IntegerField(default=0)
    chat_count = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
