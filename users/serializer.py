from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Like, Follower

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at', 'likes']

    def get_likes(self, obj):
        return obj.likes.count()


class CommentSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'post', 'created_at', 'updated_at']


class LikeSerializer(serializers.ModelSerializer):


    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']


class FollowerSerializer(serializers.ModelSerializer):


    class Meta:
        model = Follower
        fields = ['id', 'user', 'follower', 'created_at', 'is_accepted']
