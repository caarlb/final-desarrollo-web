from django.contrib import admin

from .models import Animal


# para ver los registros en admin
@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'especie', 'raza', 'edad')
