from django.urls import path
from django.contrib import admin 
from django.urls import path, include 
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()
urlpatterns = [ 
    path('blogpost/', views.post,name='post'),
    path('profile/',views.profile,name='profile'),
    path('save_post/',views.save_post,name='save_post'),
  
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)