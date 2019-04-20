import uuid

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Note(models.Model):
    note_id = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    favorite = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
