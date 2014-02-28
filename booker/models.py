from django.db import models

class Customer(models.Model):
	name= models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	message = models.CharField(max_length=120)

	def __unicode__(self):
		return u"{0}".format(self.name)

class Book (models.Model):
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	genre = models.CharField(max_length=120)
	customer = models.ManyToManyField(Customer)

	def __unicode__(self):
		return u"{0}".format(self.title)