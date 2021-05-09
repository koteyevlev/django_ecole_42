from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('worldmap/<str:action>', views.action, name='worldmap'),
    path('worldmap', views.worldmap, name='worldmap'),
    path('battle/<str:movie_id>/', views.battle, name='battle'),
    path('battle/<str:movie_id>/<str:action>', views.battle_action, name='battle'),
    path('moviedex/<str:movie_id>', views.detail),
    path('moviedex/<str:movie_id>/', views.detail),
    path('moviedex', views.moviedex, name='moviedex'),
    path('options/load_game', views.load_game, name='load'),
    path('options/load_game/<str:action>', views.load_game_action, name='load'),
    path('options/save_game', views.save_game, name='save'),
    path('options/save_game/<str:action>', views.save_game_action, name='save'),
    path('options', views.options, name='options'),
    path('', views.index, name='index')
]