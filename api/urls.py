from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r"articles", views.ArticleViewSet, basename="article")
router.register(r"authors", views.AuthorViewSet, basename="author")

urlpatterns = [
    path("", include(router.urls)),
]
