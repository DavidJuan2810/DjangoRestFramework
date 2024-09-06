from django.shortcuts import render
from .models import Tarea
from .serializers import TareaSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class TareaViewSet(ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer