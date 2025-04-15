#herramientas que se utilizan para transformar datos complejos (como objetos de una base de datos) 
# en un formato más simple y estructurado (como JSON o XML)
from rest_framework import serializers
from .models import Project

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'titulo', 'descripcion','tecnologia', 'fecha_creacion')
        read_only_fields = ('fecha_creacion', ) #para que no modifiquen la fecha de creacion
