from django.db import models

class Client(models.Model):
	name = models.CharField(max_length=30)
	phone = models.CharField(max_length = 15,unique=True)
	email = models.EmailField(unique=True)
	address = models.TextField()

