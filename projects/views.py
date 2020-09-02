from django.shortcuts import render
from django.http import HttpResponse
from .models import Members

# Create your views here.
def home(request):
	return render(request, 'projects/index.html')

def team(request):
	content = {
		'members' : Members.objects.all(),
	}
	return render(request, 'projects/our-team.html', content)

def gallery(request):
	return render(request, 'projects/gallery.html')