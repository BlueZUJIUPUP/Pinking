from django.db import models

# Create your Models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    age = models.IntegerField(default=0)


