from turtle import home
from . import views
from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from google.views import location_list_create_api_view, location_retrieve_update_delete_api_view, home_view


# Create a schema view for Swagger documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Google API Integration",
        default_version='v1',
        description="API for integrating Google Maps and Geocoding services",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', views.home_view, name='home'),
    path('api/locations/', location_list_create_api_view, name='location-list-create'),
    path('api/locations/<int:pk>/', location_retrieve_update_delete_api_view, name='location-retrieve-update-delete'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Schema JSON url
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]   