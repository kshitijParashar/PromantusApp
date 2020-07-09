from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.


class UserProfile(models.Model):
    name=models.CharField(max_length=50)
    data = JSONField(null=True)

    def __str__(self):
        return self.name


# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.DecimalField()
#     description = models.TextField()
#     release_date = models.DateField()