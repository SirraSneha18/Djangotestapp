from django.urls import path
from . import views
from quickstartproject import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.hello, name='hello'),
]
if settings.DEBUG:
    urlpatterns  +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)