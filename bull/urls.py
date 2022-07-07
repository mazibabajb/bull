
from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('about/', views.about,name="about"),
    path('pricing/', views.pricing,name="pricing"),
    path('contact/', views.contact,name="contact"),
    path('team/', views.team,name="team"),
]
