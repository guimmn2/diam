from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('votacao/', include('votacao.urls')),
    path('admin/', admin.site.urls),
]
