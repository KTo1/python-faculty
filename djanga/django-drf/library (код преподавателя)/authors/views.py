from django.shortcuts import render

# Create your views here.
from rest_framework.renderers import JSONRenderer

from rest_framework.viewsets import ModelViewSet

from .models import Author
from .serializers import AuthorModelSerializer

class AuthorModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
