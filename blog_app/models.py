from django.db import models

# Create your models here.
from auth_app.models import User


class Blog(models.Model):
    author = models.ForeignKey(User, related_name='blog', null=True, blank=True, )

    def __str__(self):
        return str(self.id)


class Category(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False, )

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False, )
    content = models.TextField(max_length=32768, null=False, blank=False, )
    rating = models.FloatField(default=0, )
    posted_date = models.DateField(auto_now_add=True, )
    update_date = models.DateField()
    blog = models.ForeignKey(Blog, related_name='posts', null=False, blank=False, )
    category = models.ForeignKey(Category, related_name='posts', null=False, blank=False, )

    def __str__(self):
        return str(self.title)


class Image(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True, )
    post = models.ForeignKey(Post, null=False, blank=True, related_name='images', )

    def __str__(self):
        return str(self.id)


class Comment(models.Model):
    content = models.TextField(max_length=32768, null=False, blank=False, )
    post = models.ForeignKey(Post, null=False, blank=False, related_name='comments', )
    author = models.ForeignKey(User, null=False, blank=False, related_name='comments', )
    date = models.DateField(auto_now_add=True, )

    def __str__(self):
        return str(self.id)


class Tag(models.Model):
    name = models.CharField(max_length=128, null=False, blank=False, )

    def __str__(self):
        return str(self.name)


class Keyword(models.Model):
    tag = models.ForeignKey(Tag, related_name='keywords', null=False, blank=False, )
    post = models.ForeignKey(Post, related_name='keywords', null=False, blank=False, )

    def __str__(self):
        return str(self.id)


class Bookmark(models.Model):
    owner = models.ForeignKey(User, null=False, related_name='bookmarks', blank=False, )
    post = models.ForeignKey(Post, null=False, related_name='bookmarks', blank=False, )

    def __str__(self):
        return str(self.id)
