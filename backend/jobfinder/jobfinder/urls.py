from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from messageapp.views import MessageModelViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Jobfinder API",
        default_version='V1.0',
        description="Документация"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()

router.register('message', MessageModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    # Auto documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]


##Пример: router.register('user', CustomUserModelViewSet). Можно зарегистрировать в едином стиле