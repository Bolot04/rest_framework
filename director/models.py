from django.db import models
from django.contrib.auth.models import User


class Director(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    duration = models.FloatField(default=0)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movies')

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, related_name='reviews')
    stars = models.IntegerField(default=1, choices=[(i, i * "*") for i in range(6)])

    def __str__(self):
        return self.text
