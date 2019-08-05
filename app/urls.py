from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from app.views import health_check, index

schema_view = get_schema_view(
    openapi.Info(
        title="Fitzme {{ project_name }} Service Documents",
        default_version='all',
        description="""
        Fitzme {{ project_name }} 입니다. 사용 가능한 {{ project_name }} API를 탐색하고 테스트할 수 있습니다.
        """,
        contact=openapi.Contact(
            name="Intellisys Co., Ltd.",
            url="http://intellisys.co.kr",
            email="intellisys@intellisys.co.kr"
        ),
    ),
    public=True,
)
urlpatterns = [
    path('', index, name='index'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0)),

    path('health/', health_check),
    path('resource/', include('app.views.resource.urls', namespace='resource')),
    path('v1/', include('app.views.v1.urls', namespace='v1')),
]
