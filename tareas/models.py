from django.db import models

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    estado = models.CharField(max_length=30,choices=[('incompleto','Incompleto'),('completo','Completo')],default='incompleto')
    def __str__(self):
        return self.titulo