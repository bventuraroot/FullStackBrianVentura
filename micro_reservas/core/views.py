# TODO DIA 1
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes

from .serializers import courts_serializer, TutorialSerializer, Partners_serializer
from .models import Bookings, Courts, Frecuency, States, Partners, Tutorial
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

# TODO DIA 2

from django.contrib.auth.models import User  # TODO Tabla User
from rest_framework.authtoken.models import Token  # Todo table Token
import json
from django.http import HttpResponse
from rest_framework.parsers import JSONParser

from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from rest_framework import generics, status


class courtsAllViewSet(generics.ListAPIView):
    queryset = Courts.objects.all()
    serializer_class = courts_serializer
    permission_classes = (IsAuthenticated,)


class registerusers(generics.CreateAPIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        usuario = request.data['username']
        correo = request.data['email']
        contra = request.data['password']
        nombre = request.data['firstname']
        apellido = request.data['lastname']
        es_staff = request.data['staff']
        nuevo_usuario = User.objects.create_user(usuario, correo, contra)
        nuevo_usuario.first_name = nombre
        nuevo_usuario.last_name = apellido
        nuevo_usuario.is_staff = es_staff
        nuevo_usuario.save()
        key_usuario = Token.objects.create(user=nuevo_usuario)
        data = {'default': 'User successfully created' + key_usuario.key}
        rpta = json.dumps(data)
        return HttpResponse(rpta, content_type='application/json')


class loginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        usuario = request.data['username']
        clave = request.data['password']
        usuario = authenticate(username=usuario, password=clave)
        if usuario:
            key_usuario = Token.objects.get(user_id=usuario.id)
            data = {
                "nombre": usuario.first_name,
                "apellido": usuario.last_name,
                "correo": usuario.email,
                "key": key_usuario.key}
        else:
            data = {"error": "Not the credentiales"}

        rpta = json.dumps(data)
        return HttpResponse(rpta, content_type='application/json')


class courtsfull(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        canchas = Courts.objects.all()
        cancha = request.GET.get('courts_id', None)
        print(cancha)
        if cancha is not None:
            canchas = canchas.filter(courts_id__icontains=cancha)
            # canchas = cancha.filters(courts_id__icontains=cancha)
        canchas_serializer = courts_serializer(canchas, many=True)
        # rpta = json.dumps(canchas_serializer)
        # return HttpResponse(rpta, content_type='application/json')
        return JsonResponse(canchas_serializer.data, safe=False)

    def post(self, request):
        # todo recibir la informacion en JSON
        canchas_data = JSONParser().parse(request)
        # todo enviando informacion a mi archivo serializer
        canchas_serializer = courts_serializer(data=canchas_data)
        if canchas_serializer.is_valid():
            # todo almacena en la BD
            canchas_serializer.save()
            return JsonResponse(canchas_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(canchas_serializer.data, status=status.HTTP_400_BAD_REQUEST)

    # Todo vistas basadas en funciones


@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Tutorial.objects.all().delete()
        return JsonResponse({'message': '{} Tutoriales delete all'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

    tutorials_serializer = TutorialSerializer(tutorials, many=True)
    return JsonResponse(tutorials_serializer.data, safe=False)


@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([AllowAny])
def tutorial_detail(request, pk):
    try:
        tutorial = Tutorial.objects.get(pk=pk)
        if request.method == 'GET':
            tutorial_serializer = TutorialSerializer(tutorial)
            return JsonResponse(tutorial_serializer.data)
        elif request.method == 'DELETE':
            tutorial.delete()
            return JsonResponse({'Message': 'Tutorial eliminado con exito'}, status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'PUT':
            tutorial_data = JSONParser().parse(request)
            tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(tutorial_serializer.data)
            return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Tutorial.DoesNotExist:

        return JsonResponse({'message': 'El Tutorial dot Not existe'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST', 'DELETE'])
def partners_serializerall(request):
    if request.method == 'GET':
        partners = Partners.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            partners = partners.filter(partners_id__icontains=name)
    elif request.method == 'POST':
        partners_data = JSONParser().parse(request)
        partners_serializer = Partners_serializer(data=partners_data)
        if partners_serializer.is_valid():
            partners_serializer.save()
            return JsonResponse(partners_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(partners_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Partners.objects.all().delete()
        return JsonResponse({'message': '{} Partners delete all'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

    partners_serializer = Partners_serializer(partners, many=True)
    return JsonResponse(partners_serializer.data, safe=False)


@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([AllowAny])
def partners_serializer(request, pk):
    try:
        partners = Partners.objects.get(partners_id=pk)
        if request.method == 'GET':
            partners_serializer = Partners_serializer(partners)
            return JsonResponse(partners_serializer.data)
        elif request.method == 'DELETE':
            partners.delete()
            return JsonResponse({'Message': 'Partners eliminado con exito'}, status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'PUT':
            partners_data = JSONParser().parse(request)
            partners_serializer = Partners_serializer(partners, data=partners_data)
            if partners_serializer.is_valid():
                partners_serializer.save()
                return JsonResponse(partners_serializer.data)
            return JsonResponse(partners_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Partners.DoesNotExist:

        return JsonResponse({'message': 'El Partners dot Not existe'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([AllowAny])
def courtsfull_detail(request, pk):
    try:
        curt = Courts.objects.get(pk=pk)
        if request.method == 'GET':
            courtsserializer = courts_serializer(curt)
            return JsonResponse(courtsserializer.data)

        elif request.method == 'DELETE':
            curt.delete()
            return JsonResponse({'Message': 'curt eliminado con exito'}, status=status.HTTP_204_NO_CONTENT)

        elif request.method == 'PUT':
            curt_data = JSONParser().parse(request)
            courtsserializer = courts_serializer(curt, data=curt_data)
            if courtsserializer.is_valid():
                courtsserializer.save()
                return JsonResponse(courtsserializer.data)
            return JsonResponse(courtsserializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Courts.DoesNotExist:
        return JsonResponse({'message': 'El Curts dot Not existe'}, status=status.HTTP_404_NOT_FOUND)
