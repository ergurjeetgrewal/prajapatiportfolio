from django.db import models
# create your models here


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    zipcode = models.CharField(max_length=6)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name+self.zipcode
