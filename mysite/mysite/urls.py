from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('', lambda request: HttpResponseRedirect('/polls/')),  # Redirige la raíz a /polls/
]