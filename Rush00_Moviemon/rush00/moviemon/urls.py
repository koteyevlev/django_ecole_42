from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('worldmap', views.worldmap, name='worldmap'),
    path('battle/<int:id>/', views.battle, name='battle'),
    path('moviedex/<int:id>/', views.detail),
    path('moviedex', views.moviedex, name='moviedex'),
    path('options/load_game', views.load_game, name='load'),
    path('options/save_game', views.save_game, name='save'),
    path('options', views.options, name='options'),
    path('', views.index, name='index')
]