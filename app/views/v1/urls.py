from django.urls import path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_jwt.views import verify_jwt_token, refresh_jwt_token


schema_view = get_schema_view(
    openapi.Info(
        title="Fitzme Account Service Documents",
        default_version='v1',
        description="""
        Fitzme Account Service입니다. 사용 가능한 Account Service API를 탐색하고 테스트할 수 있습니다.
        """,
        contact=openapi.Contact(
            name="IDS Lab.",
            url="http://intellisys.co.kr",
            email="intellisys@intellisys.co.kr"
        ),
    ),
    public=True,
)

urlpatterns = [
    # API Document
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0)),
    re_path('swagger.(json|yaml)$', schema_view.without_ui(cache_timeout=0)),
]
