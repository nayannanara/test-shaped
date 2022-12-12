from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from core.api.viewsets import PatientViewSet, ExamViewSet
from rest_framework_swagger.views import get_swagger_view

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Test Shaped API",
      default_version='v0',
      description="Test shaped",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r'core/paciente', PatientViewSet, basename='patient'),
router.register(r'core/exame', ExamViewSet, basename='exam'),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    re_path(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
