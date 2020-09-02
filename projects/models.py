from django.db import models
from PIL import Image

# Create your models here.
class Members(models.Model):
	name = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	quote = models.CharField(max_length=200, default="", editable=True)
	fb_profile = models.CharField(max_length=200, default="", editable=True)
	insta_profile = models.CharField(max_length=200, default="", editable=True)
	gmail = models.CharField(max_length=200, default="", editable=True)
	info = models.TextField()
	image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')

	def __str__(self):
		return f'{self.name} Profile'

	def save(self):
		super().save()
		img = Image.open(self.image.path)
		if img.height > 400 or img.width > 400:
			output_size = (400, 400)
			img.thumbnail(output_size)
			img.save(self.image.path)	