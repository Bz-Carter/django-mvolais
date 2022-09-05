from django_filters.rest_framework import FilterSet
from .models import Article, Product, Partner

class PartnerFilter(FilterSet):
    class Meta:
        model = Partner
        fields = {
            'alt': ['exact']
        }

class ArticleFilter(FilterSet):
    class Meta:
        model = Article
        fields = {
            'category': ['exact'],
            'tags': ['exact']
        }


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'category': ['exact'],
            'price': ['gt', 'lt']
        }