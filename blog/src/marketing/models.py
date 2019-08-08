from django.db import models

# Create your models here.

class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_noww_add=True)

    def __str__(self):
        return self.email