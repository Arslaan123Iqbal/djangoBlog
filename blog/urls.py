from django.contrib import admin
from django.urls import path, include
from blog.views import create_post, create_comment,getPosts

urlpatterns = [
    path('get/',getPosts),
    path('post/',create_post),
    path('<uuid:pk>/comment', create_comment),
]
