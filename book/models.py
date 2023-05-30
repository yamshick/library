from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    fb2 = models.FileField(upload_to='book/fb2')
    txt = models.FileField(upload_to='book/txt')
    # fb2 = models.FileField()
    # txt = models.FileField()
    def __str__(self):
        return self.title