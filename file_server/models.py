from django.db import models

class File(models.Model):
    path = models.TextField(primary_key=True)
    content = models.BinaryField()
