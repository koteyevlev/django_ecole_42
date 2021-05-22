from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.session, name='init'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_in', views.sign_in, name='sign_in'),
]