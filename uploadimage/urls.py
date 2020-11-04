from django.urls import path,include
from rest_framework import routers
from .views import UploadImageViewSet

router = routers.DefaultRouter()
router.register('upload',UploadImageViewSet)


urlpatterns = [
    path('',include(router.urls)),
]
