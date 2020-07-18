from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_403_FORBIDDEN
from rest_framework.views import APIView

from api.models import Tareas
from api.serializers import RegisterApiSerializer, TareaApiSerializer


class LoginApiView(APIView):
    permission_classes = ()

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Register
        serializer = RegisterApiSerializer(data=request.data)
        user = User.objects.all().values('username').filter(username=username)

        if len(user) == 0:
            if serializer.is_valid():
                user_ = serializer.save(
                    username=username,
                    password=make_password(password)
                )
                Token.objects.create(user=user_)

        # Login
        usuario = authenticate(username=username, password=password)

        if usuario is None:
            return Response(
                {
                    'error': 'Credenciales invalidas'
                },
                status=HTTP_403_FORBIDDEN)
        else:
            a = User.objects.filter(username=usuario).values('username', 'id')

            for i in a:
                if username == i['username']:
                    return Response({
                        "id": i['id'],
                        "username": i['username'],
                        "token": usuario.auth_token.key
                    })


class TareaApiView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        usuario = User.objects.get(username=request.user)
        tareas = Tareas.objects.filter(usuario=usuario).values('id', 'tarea', 'created')

        return Response(tareas)

    def post(self, request):
        usuario = User.objects.get(username=request.user)
        tarea = request.data.get('tarea')
        serializer = TareaApiSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(
                usuario=usuario,
                tarea=tarea
            )
            return Response({'exito': 'Tarea registrada con exito'})

        else:
            return Response({'error': 'Datos invalidos'})


class TareaDelApiView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        usuario = User.objects.get(username=request.user)
        tarea = Tareas.objects.filter(usuario=usuario).filter(id=pk)

        if tarea:
            tarea.delete()
            return Response({'exito': 'Tarea eliminada con exito'})

        else:
            return Response({'error': 'Error al intentar eliminar tarea'})

    def patch(self, request, pk):
        usuario = User.objects.get(username=request.user)

        try:
            tarea = Tareas.objects.filter(usuario=usuario).filter(id=pk).get()
            serializer = TareaApiSerializer(tarea, data=request.data, partial=True)

            if tarea and serializer.is_valid():
                serializer.save()
                return Response({'exito': 'Tarea actualizada con exito'})

            else:
                return Response({'error': 'Error al intentar actualizar tarea'})

        except ObjectDoesNotExist:
            return Response({'error': 'Error al intentar encontrar tarea'})
