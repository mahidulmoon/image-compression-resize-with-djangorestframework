from django.db import models
from django.core.files import File
from io import BytesIO
from PIL import Image
# Create your models here.
def compress_image(image):
		im = Image.open(image)
		if im.mode != 'RGB':
			im = im.convert('RGB')
		im_io = BytesIO()
		im.save(im_io, 'jpeg', quality=70,optimize=True)
		new_image = File(im_io, name=image.name)
		return new_image


class UploadImage(models.Model):
	image_field = models.ImageField(upload_to='images/',default='images/icon.png',null=False)
	created_at = models.TimeField(auto_now_add=True,blank=True)
	
	def save(self,force_insert=False, force_update=False, using=None,*args, **kwargs):
		if self.image_field:
			image = self.image_field
			if image.size > 0.3*1024*1024: #if size greater than 300kb then it will send to compress image function
				self.image_field = compress_image(image)
		super(UploadImage,self).save(*args, **kwargs)
	

	
