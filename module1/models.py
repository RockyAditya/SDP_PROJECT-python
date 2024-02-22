from django.db import models

# from .tpm.module1 import forms


# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    phonenumber = models.IntegerField()

    class Meta:
        db_table = "Register"


class contactus(models.Model):
    firstname = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    lastname = models.CharField(max_length=100)
    comment = models.TextField(max_length=300)

    class Meta:
        db_table = "contactus"

