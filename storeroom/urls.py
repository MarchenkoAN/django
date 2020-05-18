from django.urls import path
from . import views
app_name = 'storeroom'
urlpatterns = [
   # и т.д. пишешшь више чем нижняя строка
    path('', views.index, name='index'),
]