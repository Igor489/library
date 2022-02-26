"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from userapp.views import UserViewSet
from todoapp.views import ToDoViewSet, ProjectViewSet
from rest_framework.schemas import get_schema_view as gsv

router = routers.DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)
router.register('users', UserViewSet)
router.register('todos', ToDoViewSet)
router.register('projects', ProjectViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="API documentation",
      default_version='1.0',
      # description="Test description",
      # terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="admin@admin.local"),
      # license=openapi.License(name="BSD License"),
   ),
   public=True,
   # permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('openapi', gsv(
        title="TODOMONSTER",
        description="API for all things …",
        version="1.0"
    ), name='openapi-schema'),

    path('my-swagger-ui/', TemplateView.as_view(
        template_name='todoapp/swagger.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),

    path('my-redoc/', TemplateView.as_view(
        template_name='todoapp/redoc.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='redoc'),
]
