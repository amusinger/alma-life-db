from django.conf.urls import url, include
from django.contrib import admin

from blog_app.views import blog_list, post_list

urlpatterns = [
    url(r'^blogs/$', blog_list),
    url(r'^posts/$', post_list),
]
