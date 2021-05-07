from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('django', views.django, name='django'),
    path('display', views.display, name='display'),
    path('templates', views.templates, name='templates'),
    path('', views.index, name='index')
]