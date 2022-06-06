from django.db import models
from django.contrib.auth.models import User


class Folder(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Note(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    # title = models.CharField(max_length=255)
    content = models.TextField()
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:50]