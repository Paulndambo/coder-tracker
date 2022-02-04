from xml.etree.ElementInclude import include
from django.urls import path, include
from . views import ActivityViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("activities", ActivityViewSet, basename="activties")

urlpatterns = [
    path("", include(router.urls)),
]