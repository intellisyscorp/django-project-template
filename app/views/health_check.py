from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


@swagger_auto_schema(
    method='get',
    operation_id="API Health check",
    operation_description="API 정상 작동 여부를 확인 가능합니다.",
    responses={
        200: "정상",
    },
    tags=['Info']
)
@api_view(['GET'])
@permission_classes((permissions.AllowAny, ))
def health_check(request):
    return Response({
        "status": "UP"
    }, status=status.HTTP_200_OK)
