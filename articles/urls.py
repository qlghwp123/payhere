from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('duplicate/<int:pk>/', views.duplicate, name='duplicate'),
    path('index/', views.index, name='index'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]
