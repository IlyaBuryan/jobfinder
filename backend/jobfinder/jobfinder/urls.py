from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from companyapp.views import CompanyCardModelViewSet, CompanyCardListView, CompanyCardCreateView, \
    CompanyCardDetailView, VacancyModelViewSet, VacancyListView, VacancyCreateView, VacancyDetailView

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
router.register('companyapp', CompanyCardModelViewSet)
router.register('vacancyapp', VacancyModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    #company
    path('api/v1/companies', CompanyCardListView.as_view()),
    path('api/v1/company/create/', CompanyCardCreateView.as_view()),
    path('api/v1/company/detail/<int:pk>/', CompanyCardDetailView.as_view()),
    #vacancy
    path('api/v1/vacancies', VacancyListView.as_view()),
    path('api/v1/vacancy/create/', VacancyCreateView.as_view()),
    path('api/v1/vacancy/detail/<int:pk>/', VacancyDetailView.as_view()),

# Auto documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]
