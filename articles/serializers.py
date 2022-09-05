from rest_framework import serializers

from .models import Article, Tag, Category, Photo, Product, Service, Portfolio, Partner


class PhotoSerializer(serializers.ModelSerializer):
    """Serializer for Photo object"""
    class Meta:
        model = Photo
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    """Serializer for Article object"""
    class Meta:
        model = Article
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product object"""
    class Meta:
        model = Product
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    """Serializer for Service object"""
    class Meta:
        model = Service
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    """Serializer for Portfolio object"""
    class Meta:
        model = Portfolio
        fields = '__all__'


class PartnerSerializer(serializers.ModelSerializer):
    """Serializer for Partner object"""
    class Meta:
        model = Partner
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag object"""

    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for category object"""

    class Meta:
        model = Category
        fields = '__all__'
