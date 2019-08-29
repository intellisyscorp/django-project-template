from django.db.models import Model
from rest_framework.viewsets import ModelViewSet
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema


def fitzme_resource(ResourceModel: Model):
    def inner(ResourceViewSet: ModelViewSet):

        ModelNameEn = ResourceModel.__name__
        ModelNameKo = ResourceModel._meta.verbose_name

        @method_decorator(name='list', decorator=swagger_auto_schema(
            operation_id=f'{ModelNameEn} list',
            operation_description=f'{ModelNameKo} 정보 리스트를 반환합니다.',
            tags=[f'Resource {ModelNameEn}'],
        ))
        @method_decorator(name='retrieve', decorator=swagger_auto_schema(
            operation_id=f'{ModelNameEn} retrieve',
            operation_description=f'특정 {ModelNameKo} 정보를 반환합니다.',
            tags=[f'Resource {ModelNameEn}'],
        ))
        @method_decorator(name='create', decorator=swagger_auto_schema(
            operation_id=f'{ModelNameEn} create',
            operation_description=f'특정 {ModelNameKo} 정보를 생성합니다.',
            tags=[f'Resource {ModelNameEn}'],
        ))
        @method_decorator(name='update', decorator=swagger_auto_schema(
            operation_id=f'{ModelNameEn} update',
            operation_description=f'특정 {ModelNameKo} 정보를 수정합니다.',
            tags=[f'Resource {ModelNameEn}'],
        ))
        @method_decorator(name='partial_update', decorator=swagger_auto_schema(
            operation_id=f'{ModelNameEn} partial_update',
            operation_description=f'특정 {ModelNameKo} 정보의 일부를 수정합니다.',
            tags=[f'Resource {ModelNameEn}'],
        ))
        @method_decorator(name='destroy', decorator=swagger_auto_schema(
            operation_id=f'{ModelNameEn} destroy',
            operation_description=f'특정 {ModelNameKo} 정보를 삭제합니다.',
            tags=[f'Resource {ModelNameEn}'],
        ))
        class ResourceViewSetWrapper(ResourceViewSet):
            pass

        return ResourceViewSetWrapper
    return inner
