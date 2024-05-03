from django.contrib import admin
from .models import Post, Comment, Like, Follower
# Register your models here.

admin.site.register(Post)
admin.site.register(Follower)
admin.site.register(Like)
admin.site.register(Comment)