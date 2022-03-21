from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about_us, name='about-us'),
    path('create', views.create, name='create'),
    path('comments_all', views.comments_all, name='comments_all'),
]
