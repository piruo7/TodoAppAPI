from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from api.models import Tareas


class RegisterApiSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class TareaApiSerializer(ModelSerializer):
    class Meta:
        model = Tareas
        fields = ('tarea',)

