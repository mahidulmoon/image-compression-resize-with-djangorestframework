from django.shortcuts import render
from .models import UploadImage
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UploadImageSerializer
# Create your views here.


class UploadImageViewSet(viewsets.ModelViewSet):
    queryset = UploadImage.objects.all()
    serializer_class = UploadImageSerializer