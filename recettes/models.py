import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


class Recipe(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=1500)
    pub_date = models.DateTimeField('date published')
    has_ingredients = models.ManyToManyField('Has_Ingredient')
    has_tags = models.ManyToManyField('Has_Tag')

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


class Has_Ingredient(models.Model):
    quantity = models.IntegerField(default=0)
    ingredient = models.ManyToManyField('Ingredient')
    kitchen = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    pass


class Ingredient(models.Model):
    name = models.CharField(max_length=150)
    measure = models.CharField(max_length=15, default="")

    def __str__(self):
        return self.name


class Has_Tag(models.Model):
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)
    kitchen = models.ForeignKey('Recipe', on_delete=models.CASCADE)

    def __str__(self):
        return self.tag.name


class Tag(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
