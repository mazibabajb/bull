
from django.contrib import admin
from django.urls import path
from django.urls.conf import re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('about/', views.about,name="about"),
    path('pricing/', views.pricing,name="pricing"),
    path('contact/', views.contact,name="contact"),
    path('team/', views.team,name="team"),
    path('blog/', views.blog,name="blog"),
    path('analysis/', views.analysis,name="analysis"),
    path('blogsearchbar/',views.blogsearchbar, name="blogsearchbar"),
    path('emailsubscription/',views.emailsubscription, name="emailsubscription"),
    path('blog/<int:id>/',views.post_detail, name ='post_detail'),
    path('analysis/<int:id>/',views.analysis_detail, name ='analysis_detail'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
]
