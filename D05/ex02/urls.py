from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('init', views.init, name='init'),
    path('populate', views.populate, name='init'),
    path('display', views.display, name='init'),
]