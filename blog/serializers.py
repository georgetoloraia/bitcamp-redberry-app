# blog/serializers.py
from rest_framework import serializers
from .models import Category, Blog

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):

    category = CategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Blog
        fields = '__all__'
