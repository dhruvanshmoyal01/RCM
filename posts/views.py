from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.
def posts(request):
	content = {
		'posts' : Post.objects.all(),
	}
	return render(request, 'posts/our-projects.html', content)