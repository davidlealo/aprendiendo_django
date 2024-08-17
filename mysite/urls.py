# mysite/urls.py
from django.contrib import admin
from django.urls import path, include
from polls import views as polls_views  # Importar views desde polls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', polls_views.index, name='index'),  # Ruta para la vista index en la raíz
]
