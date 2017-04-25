from django.contrib import admin

# Register your models here.
from blog_app.models import Blog, Post, Category, Tag, Keyword, Comment, Bookmark, Image

admin.site.register(Blog)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Keyword)
admin.site.register(Comment)
admin.site.register(Bookmark)
admin.site.register(Image)