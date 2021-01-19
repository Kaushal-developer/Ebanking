from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50, default="")
    email = models.EmailField(unique=True)
    mobile = models.IntegerField(unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name