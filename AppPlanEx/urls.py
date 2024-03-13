from django.urls import path
from . import views

from quickstartproject import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home, name="Home"),
    #path('Home/', views.Home, name="Home"),
    path('appplanex/', views.Home, name="appplanex"), 
]

if settings.DEBUG:
    urlpatterns  +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
