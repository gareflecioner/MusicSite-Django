from django.db import models

# Create your models here.


class Musicians(models.Model):
    name=models.CharField(max_length=255)
    about=models.TextField(blank=True)
    photo=models.ImageField(upload_to='photos/musicians/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update =models.DateTimeField(auto_now=True)
    is_published=models.BooleanField(default=True)

class Albums(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField(blank=True)
    photo=models.ImageField(upload_to='photos/albums/%Y/%m/%d/')
    time_create=models.DateTimeField(auto_now_add=True)
    time_update =models.DateTimeField(auto_now=True)
    is_published =models.BooleanField(default=True)
    genre=models.ManyToManyField('Genre')
    author=models.ForeignKey('Musicians',on_delete=models.PROTECT)


class Genre(models.Model):
    name=models.CharField(max_length=100,db_index=True)

    def __str__(self):
        return self.name
