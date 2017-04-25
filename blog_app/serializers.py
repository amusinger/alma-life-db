from rest_framework import serializers

from auth_app.models import User
from blog_app.models import Blog, Post, Category, Comment, Keyword, Tag


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'description',)


class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False)

    class Meta:
        model = Blog
        fields = ('author',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False)

    class Meta:
        model = Comment
        fields = ('content', 'author', 'date',)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class KeywordSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=False)

    class Meta:
        model = Keyword
        fields = ('tag',)


class PostSerializer(serializers.ModelSerializer):
    blog = BlogSerializer(many=False)
    category = CategorySerializer(many=False)
    comments = CommentSerializer(many=True)
    keywords = KeywordSerializer(many=True)

    class Meta:
        model = Post
        fields = (
        'comments', 'title', 'content', 'posted_date', 'update_date', 'blog', 'category', 'keywords', 'images',)
