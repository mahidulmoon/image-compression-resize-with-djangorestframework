from django.db import models

# Create your models here.

class UploadImage(models.Model):
	image_field = models.ImageField(upload_to='images/',default='images/icon.png')
	created_at = models.TimeField(auto_now_add=True,blank=True)