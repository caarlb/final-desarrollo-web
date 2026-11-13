from django.db import models


# Tabla de animales con sus 4 atributos 
class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=60)
    raza = models.CharField(max_length=80)
    edad = models.PositiveIntegerField()  # positivo porque no existe la edad negativas

    # estas dos las llena django solito
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'animales'  # nombre de la tabla 
        ordering = ['id']

    # para que en el admin se vea el nombre 
    def __str__(self):
        return self.nombre
