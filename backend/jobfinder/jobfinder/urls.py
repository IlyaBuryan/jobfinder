from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from workerapp.views import WorkerModelViewSet, ResumeModelViewSet

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
router.register('worker', WorkerModelViewSet)
router.register('resume', ResumeModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auto documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    path('api/v1/worker/create/', WorkerModelViewSet.as_view({'post': 'create'})),
    path('api/v1/worker/<int:pk>/', WorkerModelViewSet.as_view({'get': 'retrieve'})),
    path('api/v1/resume/create/', ResumeModelViewSet.as_view({'post': 'create'})),
    path('api/v1/resume/<int:pk>/', ResumeModelViewSet.as_view({'get': 'retrieve'})),
]
