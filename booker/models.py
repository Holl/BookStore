from django.db import models


class Book (models.Model):
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	genre = models.CharField(max_length=120)

	def __unicode__(self):
		return u"{0}".format(self.title)

class Customer(models.Model):
	name= models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	message = models.CharField(max_length=120)
	book = models.ManyToManyField(Book)

	def __unicode__(self):
		return u"{0}".format(self.name)

