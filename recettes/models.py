import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=1500)
    pub_date = models.DateTimeField('date published')
    ingredients = models.ManyToManyField('Ingredient', related_name='recipes')
    tags = models.ManyToManyField('Tag', related_name='recipes')

    def __str__(self):
        return self.title

    @admin.display(
        boolean=True,
        ordering=('title',),
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Ingredient(models.Model):
    name = models.CharField(max_length=150)
    measure = models.CharField(max_length=30, default="nb")
    quantity = models.IntegerField(default=0)
    recipes_id = models.ForeignKey('Recipe', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=150)
    recipes_id = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    icon = models.CharField(max_length=150, default="fa-solid fa-utensils")

    def __str__(self):
        return self.name
