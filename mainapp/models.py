from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=64, unique=True)
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=64, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
