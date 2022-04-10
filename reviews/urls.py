import re
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.dashboard,name='dashboad'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('search', views.search_results, name='search_results')
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)