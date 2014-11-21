from django.db import models

# Create your models here.
class Tags(models.Model):
	name = models.CharField('tags', max_length=50)

	def __unicode__(self):
		return self.name


class Post(models.Model):
	title = models.CharField('Titulo', max_length=50)
	text = models.TextField('Texto')
	tags = models.ManyToManyField(Tags)

	def __unicode__(self):
		return self.title
