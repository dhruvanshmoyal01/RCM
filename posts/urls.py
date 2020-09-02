from django.urls import path
from . import views 

urlpatterns = [
    path('our-projects/', views.posts, name = 'our-projects'),
]