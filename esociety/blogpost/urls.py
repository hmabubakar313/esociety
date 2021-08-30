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
    path('feed/',views.feed,name='feed'),
    path('extended_feed/<int:id>/',views.extended_feed,name='extended_feed')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)