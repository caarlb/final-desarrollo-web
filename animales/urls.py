from django.urls import path

from .views import AnimalDetalle, AnimalLista

urlpatterns = [
    path('animales/', AnimalLista.as_view(), name='animal-lista'),
    path('animales/<int:pk>/', AnimalDetalle.as_view(), name='animal-detalle'),
]
