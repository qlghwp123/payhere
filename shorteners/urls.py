from django.urls import path
from . import views

app_name = 'shorteners'

# link : https://ninano1109.tistory.com/63
urlpatterns = [
    path('', views.shortener, name='shortener'),
    path('<str:new>/', views.original, name='original')
]
