# polls/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la vista index
    path('despedida/', views.despedida, name="despedida")
]