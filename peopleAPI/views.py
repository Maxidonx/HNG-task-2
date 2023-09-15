from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser, FormParser
from .models import Person
from .serializers import PersonSerializer
from django.shortcuts import get_object_or_404

class PersonViewset(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    @parser_classes([JSONParser, FormParser])
    def create(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @parser_classes([JSONParser, FormParser])
    def update(self, request, pk=None):
        try:
            if pk.isdigit():
                instance = Person.objects.get(id=pk)
            else:
                instance = Person.objects.get(fullname=pk)

            serializer = PersonSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Person.DoesNotExist:
            return Response({'detail': 'Person not found.'}, status=status.HTTP_404_NOT_FOUND)
