from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
	ARTIST_TYPE = (
		('PHOTO', 'Photographer'),
		('PAINTER', 'Painter')
	)

	GENDER_CHOICES = (
		#(actual value, human readable name)
		('M', 'Male'),
		('F', 'Female'),
		('O', 'Other')
	)
	user = models.OneToOneField(User)
	avatar = models.URLField(max_length=256)
	first_name = models.CharField(max_length=64, blank=True)
	last_name = models.CharField(max_length=64, blank=True)
	nick_name = models.CharField(max_length=64)
	birth_date = models.DateField(auto_now=False, blank=True)

	gender = models.CharField(
		max_length=2,
		choices=GENDER_CHOICES,
		default='M')

	type = models.CharField(
		max_length=32,
		choices=ARTIST_TYPE,
		default='PHOTO')

	description = models.TextField(max_length=1024, blank=True)

	def __unicode__(self):
		return "User: " + str(self.user) + ", Name: " + self.nick_name  

class Item(models.Model):
	name = models.CharField(max_length=64)
	description = models.TextField(max_length=1024)
	creator = models.ForeignKey(
		'Artist',
		on_delete=models.CASCADE,
		)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	avatar = models.URLField(max_length=256)

	def __unicode__(self):
		return "Name: " + self.name + ", Artist: " + self.creator.nick_name

class Photo(models.Model):
	name = models.CharField(max_length=64)
	description = models.TextField(max_length=1024)
	creator = models.ForeignKey(
		'Artist',
		on_delete=models.CASCADE,
		)
	item = models.ForeignKey(
		'Item',
		on_delete=models.CASCADE,
		)


