from django.db import models
from django.utils import timezone
from PIL import Image

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	tag = models.CharField(max_length=50)
	date = models.DateTimeField(default = timezone.now)
	info = models.TextField()
	image = models.ImageField(default = 'default.jpg', upload_to = 'projects_pics')

	def __str__(self):
		return f'{self.title}'

	def save(self):
		super().save()
		img = Image.open(self.image.path)
		if img.height > 500 or img.width > 500:
			output_size = (500, 500)
			img.thumbnail(output_size)
			img.save(self.image.path)