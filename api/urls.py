from django.urls import path, include
from rest_framework import routers
from api import apiviews as viewsets

router = routers.DefaultRouter()
router.register(r"owners", viewsets.OwnerViewSet)
router.register(r"species", viewsets.SepciesViewSet)
# router.register(r"users", viewsets.UserViewSet, basename="user")


urlpatterns = [
    path("", include(router.urls)),
]
