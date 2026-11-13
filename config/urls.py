from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # todas las rutas inician con  /api/
    path('api/', include('animales.urls')),
]
