from django.db import models

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.username