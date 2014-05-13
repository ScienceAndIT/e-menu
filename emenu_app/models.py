from django.db import models

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name


class Danie(models.Model):
    menu = models.ForeignKey(Menu)
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=200)
    views = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='food_images', blank=True)

    def __unicode__(self):
        return self.title


class Error(models.Model):
    message = models.TextField(max_length=200)
    email = models.EmailField(max_length=128)

    def __unicode__(self):
        return self.message