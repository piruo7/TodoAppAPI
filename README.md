# TODO APP API

#### python manage.py migrate
#### python manage.py createsuperuser
#### python manage.py runserver

## LOGIN / REGISTER
##### http://127.0.0.1:8000/api/v1/login/ - POST
##### REQUEST
```
{
    "username": "username",
    "password": "password"
}
```
---
##### RESPONSE
```
{
    "id": <int>,
    "username": "username",
    "token": "TOKEN"
}
```

## TAREAS
##### http://127.0.0.1:8000/api/v1/tarea/ - GET
##### REQUEST
```
Authorization Token TOKEN
```
---
##### RESPONSE
```
[
    {
        "id": <int>,
        "tarea": "TAREA",
        "created": "2020-07-18T02:49:15.556889Z"
    }
]
```
##### http://127.0.0.1:8000/api/v1/tarea/ - POST
##### REQUEST
```
Authorization Token TOKEN

{
    "tarea": "Mi nueva tarea"
}
```
---
##### RESPONSE
```
{
    "exito": "Tarea registrada con exito"
}
```
---
```
{
    "error": "Datos invalidos"
}
```
##### http://127.0.0.1:8000/api/v1/tarea/<pk>/ - PATCH
##### REQUEST
```
Authorization Token TOKEN

{
    "tarea": "Mi nueva tarea"
}
```
---
##### RESPONSE
```
{
    "exito": "Tarea actualizada con exito"
}
```
---
```
{
    "error": "Error al intentar actualizar tarea"
}
```

##### http://127.0.0.1:8000/api/v1/tarea/<pk>/ - DELETE
##### REQUEST
```
Authorization Token TOKEN
```
---
##### RESPONSE
```
{
    "exito": "Tarea eliminada con exito"
}
```
---
```
{
    "error": "Error al intentar eliminar tarea"
}
```
