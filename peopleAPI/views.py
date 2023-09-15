from rest_framework import viewsets, status, parsers
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
from django.shortcuts import get_object_or_404

class PersonViewset(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    parser_classes = [parsers.MultiPartParser, parsers.JSONParser, parsers.FormParser]  # Handle multiple content types

    def retrieve(self, request, pk=None):
        # Try to retrieve by id first
        if pk.isdigit():
            person = get_object_or_404(Person, id=pk)
        else:
            # If not a valid integer, assume it's a fullname
            person = get_object_or_404(Person, fullname=pk)

        serializer = PersonSerializer(person)
        return Response(serializer.data)

    def create(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        # Attempt to retrieve by id
        if pk.isdigit():
            instance = get_object_or_404(Person, id=pk)
        else:
            # If not a valid integer, assume it's a fullname
            instance = get_object_or_404(Person, fullname=pk)

        serializer = PersonSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        # Attempt to retrieve by id
        if pk.isdigit():
            instance = get_object_or_404(Person, id=pk)
        else:
            # If not a valid integer, assume it's a fullname
            instance = get_object_or_404(Person, fullname=pk)

        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
