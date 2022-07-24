from django.urls import path

from . import views

app_name = 'recettes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:recette_id>/', views.detail, name='detail'),
    path('about/', views.about, name='about'),
    path('add/', views.add, name='add'),
]