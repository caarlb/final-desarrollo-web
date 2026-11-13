from rest_framework import serializers

from .models import Animal


# El serializer convierte el objeto de la bd a json en los dos sentidos
# y validas que los campos obligatorios vengan.
class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = [
            'id',
            'nombre',
            'especie',
            'raza',
            'edad',
            'created_at',
            'updated_at',
        ]
