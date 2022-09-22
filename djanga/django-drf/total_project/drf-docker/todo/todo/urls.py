"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import permissions
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from usersapp.views import UserModelViewSet
from todoapp.views import ProjectModelViewSet, ToDoModelViewSet

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from graphene_django.views import GraphQLView


schema_view = get_schema_view(
    openapi.Info(
        title="ToDo with",
        default_version='1.0',
        description="Really fresh documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny]

)

router = DefaultRouter()
router.register('users', UserModelViewSet, basename='users')
router.register('projects', ProjectModelViewSet, basename='projects')
router.register('todos', ToDoModelViewSet, basename='todo')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('swagger<str:format>/', schema_view.without_ui(cache_timeout=0)),
    path('swagger/', schema_view.with_ui('swagger')),
    path('redoc/', schema_view.with_ui('redoc')),
    path('graphql/', GraphQLView.as_view(graphiql=True)),

    path('', TemplateView.as_view(template_name='index.html')),
]
