from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializers

class ProjectViewSet(viewsets.ModelViewSet):  #aca decimos que consultas se van a poder hacer
    queryset = Project.objects.all() #conjunto de datos
    permission_classes = [permissions.AllowAny] #cualquier cliente va a poder solicitar datos a mi servidor
    serializer_class = ProjectSerializers