from django.urls import path, include

from app.views import health_check

urlpatterns = [
    path('health/', health_check),
    path('v1/', include('app.views.v1.urls')),
]
