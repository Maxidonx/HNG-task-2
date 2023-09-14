from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
from django.shortcuts import get_object_or_404

class PersonViewset(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def retrieve(self, request, pk=None):
        try:
            if pk.isdigit():
                person = Person.objects.get(id=pk)
            else:
                person = Person.objects.get(fullname=pk)
            serializer = PersonSerializer(person)
            return Response(serializer.data)
        except Person.DoesNotExist:
            return Response({'detail': 'Person not found.'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

    def destroy(self, request, pk=None):
        try:
            if pk.isdigit():
                instance = Person.objects.get(id=pk)
            else:
                instance = Person.objects.get(fullname=pk)

            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Person.DoesNotExist:
            return Response({'detail': 'Person not found.'}, status=status.HTTP_404_NOT_FOUND)
