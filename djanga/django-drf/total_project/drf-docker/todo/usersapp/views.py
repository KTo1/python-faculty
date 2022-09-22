from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet
from djangorestframework_camel_case.render import CamelCaseJSONRenderer

from usersapp.models import User
from usersapp.serializers import UserModelSerializer, UserStaffModelSerializer


class UserModelViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    # renderer_classes = [CamelCaseJSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def get_serializer_class(self):
        if self.request.version == '1.0':
            return UserModelSerializer
        return UserStaffModelSerializer

