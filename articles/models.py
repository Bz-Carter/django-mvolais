from mvolaisGroup import settings
from django.db import models
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    """slug = models.SlugField(max_length=100, unique=True)"""

    class Meta:
        """verbose_name = 'category'"""
        verbose_name_plural = 'categories'


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    """slug = models.SlugField(max_length=100, unique=True)"""


class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    """slug = models.SlugField(max_length=200, unique=True)"""
    description = models.TextField(max_length=200, blank=True, default='')
    body = models.TextField(blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='articles', on_delete=models.CASCADE)
    image = models.CharField(max_length=200)
    created = models.DateTimeField()

    class Meta:
        ordering = ['-created']


class Photo(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.CharField(max_length=200)
    alt = models.TextField(max_length=200, blank=True, default='')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='photos', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']


class Partner(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.CharField(max_length=200)
    alt = models.TextField(max_length=200, blank=True, default='')
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']


class Service(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.CharField(max_length=200)
    body = models.TextField(blank=True, default='')
    description = models.TextField(max_length=200, blank=True, default='')
    created = models.DateTimeField(auto_now=True)


class Portfolio(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=200, blank=True, default='')
    body = models.TextField(blank=True, default='')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    client = models.CharField(max_length=200, blank=True, default='')
    photos = models.ManyToManyField('Photo')
    image = models.CharField(max_length=200)
    created = models.DateTimeField()

    class Meta:
        ordering = ['-created']


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photos = models.ManyToManyField('Photo')
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
