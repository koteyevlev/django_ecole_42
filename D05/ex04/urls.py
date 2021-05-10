from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('init', views.init, name='init'),
    path('populate', views.populate, name='populate'),
    path('display', views.display, name='display'),
    path('remove', views.remove, name='remove'),
]