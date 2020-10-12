from django.shortcuts import render
from .models import UploadImage
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UploadImageSerializer
# Create your views here.


class UploadImageViewSet(viewsets.ModelViewSet):
    queryset = UploadImage.objects.all()
    serializer_class = UploadImageSerializer

    def create(self, request, *args, **kwargs):
        file = request.FILES['image_field']
        image = UploadImage.objects.create(image_field=file)
        #image.save()
        return Response({'message': "Uploaded","image_url" : image.image_field.url}, status=200)