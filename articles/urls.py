from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import (
ArticleGenericAPIView, FileUploadView, CategoryGenericAPIView, TagGenericAPIView,
PhotoGenericAPIView, ProductGenericAPIView, PublicProductGenericAPIView,
PublicArticleGenericAPIView, PublicPhotoGenericAPIView, PublicCategoryGenericAPIView,
PublicTagGenericAPIView, ServiceGenericAPIView, PublicServiceGenericAPIView,
PortfolioGenericAPIView, PublicPortfolioGenericAPIView, PartnerGenericAPIView,
PublicPartnerGenericAPIView
)

urlpatterns = [
    path('articles', ArticleGenericAPIView.as_view()),
    path('article', PublicArticleGenericAPIView.as_view()),
    path('articles/<str:pk>', ArticleGenericAPIView.as_view()),
    path('article/<str:pk>', PublicArticleGenericAPIView.as_view()),
    path('products', ProductGenericAPIView.as_view()),
    path('product', PublicProductGenericAPIView.as_view()),
    path('products/<str:pk>', ProductGenericAPIView.as_view()),
    path('product/<str:pk>', PublicProductGenericAPIView.as_view()),
    path('services', ServiceGenericAPIView.as_view()),
    path('service', PublicServiceGenericAPIView.as_view()),
    path('services/<str:pk>', ServiceGenericAPIView.as_view()),
    path('service/<str:pk>', PublicServiceGenericAPIView.as_view()),
    path('portfolios', PortfolioGenericAPIView.as_view()),
    path('portfolio', PublicPortfolioGenericAPIView.as_view()),
    path('portfolios/<str:pk>', PortfolioGenericAPIView.as_view()),
    path('portfolio/<str:pk>', PublicPortfolioGenericAPIView.as_view()),
    path('partners', PartnerGenericAPIView.as_view()),
    path('partner', PublicPartnerGenericAPIView.as_view()),
    path('partners/<str:pk>', PartnerGenericAPIView.as_view()),
    path('partner/<str:pk>', PublicPartnerGenericAPIView.as_view()),
    path('upload', FileUploadView.as_view()),
    path('categories', CategoryGenericAPIView.as_view()),
    path('category', PublicCategoryGenericAPIView.as_view()),
    path('categories/<str:pk>', CategoryGenericAPIView.as_view()),
    path('category/<str:pk>', PublicCategoryGenericAPIView.as_view()),
    path('tags', TagGenericAPIView.as_view()),
    path('tag', PublicTagGenericAPIView.as_view()),
    path('tags/<str:pk>', TagGenericAPIView.as_view()),
    path('tag/<str:pk>', PublicTagGenericAPIView.as_view()),
    path('photos', PhotoGenericAPIView.as_view()),
    path('photo', PublicPhotoGenericAPIView.as_view()),
    path('photos/<str:pk>', PhotoGenericAPIView.as_view()),
    path('photo/<str:pk>', PublicPhotoGenericAPIView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)