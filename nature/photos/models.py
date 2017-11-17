from django.db import models
import datetime as dt

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()


    def __str__(self):
        return self.first_name + ' ' +self.last_name


class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name




class Post(models.Model):
    post_img = models.ImageField(upload_to = 'photos/')
    upd_date = models.DateTimeField(auto_now_add=True)
    img_desc = models.CharField(max_length=255)
    tags = models.ManyToManyField(tags)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.img_desc


    
