from django.db import models
from django.http import HttpResponse

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    pwd = models.CharField(max_length=50)
    
    def convert_to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "pwd": self.pwd
        }
    