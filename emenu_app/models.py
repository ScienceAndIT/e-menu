from django.db import models

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name


class Danie(models.Model):
    menu = models.ForeignKey(Menu)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=200)
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title