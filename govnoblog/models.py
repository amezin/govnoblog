from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User)
    datetime = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=255)

    def __str__(self):
        return str(self.user) + ': ' + self.content

    class Meta:
        ordering = ['-datetime']

