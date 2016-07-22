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
	active = models.BooleanField(default=False)

	gender = models.CharField(
		max_length=2,
		choices=GENDER_CHOICES,
		default='M')

	type = models.CharField(
		max_length=32,
		choices=ARTIST_TYPE,
		default='PHOTO')

	one_sentence_description = models.TextField(max_length=1024, blank=True)
	description_title = models.CharField(max_length=256, blank=True, default="")
	description = models.TextField(max_length=40960, blank=True)

	def __unicode__(self):
		return "User: " + str(self.user) + ", Name: " + self.nick_name  

	def jsObject(self):
		return {
            "id": self.id,
            "nickname": self.nick_name,
            "description": self.description,
            "img_url": self.avatar,
            "one_sentence_description": self.one_sentence_description,
        }

class Item(models.Model):
	name = models.CharField(max_length=64)
	description = models.TextField(max_length=40960)
	creator = models.ForeignKey(
		'Artist',
		on_delete=models.CASCADE,
		)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	avatar = models.URLField(max_length=256)
	type = models.CharField(max_length=64, default="Paint")
	year = models.IntegerField(default=2016)
	size = models.CharField(max_length=64, default="1 X 1")
	buy_link = models.URLField(max_length=256, default="")

	def __unicode__(self):
		return "Name: " + self.name + ", Artist: " + self.creator.nick_name

	def jsObject(self):
		return {
        	"id": self.id,
        	"name": self.name,
        	"description": self.description,
        	"price": self.price,
        	"creator_name": self.creator.nick_name,
        	"creator_id": self.creator.id,
        	"creator_description": self.creator.one_sentence_description,
        	"creator_avatar_url": self.creator.avatar,
        	"img_url": self.avatar,
        	"type": self.type,
        	"year": self.year,
        	"size": self.size,
        	"buy_link": self.buy_link,
        }

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


