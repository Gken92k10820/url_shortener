from django.urls import path
from . import views

app_name = 'shortener'
urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.create, name='create'),
    path('<str:pk>', views.go, name='go'),
]