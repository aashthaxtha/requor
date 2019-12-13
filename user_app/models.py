from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class UserModel(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    reputation = models.PositiveIntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return (self.name)



