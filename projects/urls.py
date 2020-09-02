from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name = 'home-page'),
    path('our-team/', views.team, name = 'our-team'),
    path('gallery/', views.gallery, name = 'gallery'),
]