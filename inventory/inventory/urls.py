from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
schema_view = get_schema_view(
   openapi.Info(
      title="InventoryManagement REST API",
      default_version='v1',
      description="Inventory Tracker API With DRF To Practice CRUD Operations And Serializer Basics.",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('inventory/restapis/',include('restapi.urls')),
]
