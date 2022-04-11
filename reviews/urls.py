import re
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.dashboard,name='dashboad'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('search', views.search_results, name='search_results'),
    path('profile', views.profile,name="profile"),
    path('api/profile', views.ProfileMerch.as_view()),
    path('api/project', views.ProjectMerch.as_view()),

    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)