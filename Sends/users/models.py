from django.db import models

class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=256)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return f"{self.username} {self.id}"