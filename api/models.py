from django.contrib.auth.models import User
from django.db import models


class Tareas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tarea = models.CharField(max_length=256)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Tareas"

    def __str__(self):
        return self.tarea
