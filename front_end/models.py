from django.db import models


# Create your models here.
class Publication(models.Model):
    publication_name = models.CharField(max_length=500, help_text='Publication name')
    publication_url = models.URLField(null=True)

    def __str__(self):
        return self.publication_name


class Book(models.Model):
    book_name = models.CharField(max_length=500, help_text='Book name')
    book_url = models.URLField(null=True)

    def __str__(self):
        return self.book_name


class Conference(models.Model):
    conference_name = models.CharField(max_length=500, help_text='Book name')
    conference_url = models.URLField(null=True)

    def __str__(self):
        return self.conference_name