from rest_framework import generics

from .models import Animal
from .serializers import AnimalSerializer


# GET  devuelve la lista
# POST  crea un animal nuevo
class AnimalLista(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


# GET  consulta uno
# PUT  actualiza
# DELETE  elimina
# Si el id no existe, responde 404 
class AnimalDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
