from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('process/', include(('external_service.urls', 'external_service'), namespace='external_service')),
]
