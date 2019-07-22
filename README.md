# How to use

Django project를 생성할 때 다음과 같이 입력할 경우 template대로 자동 생성됨.
``` bash
django-admin startproject \
    --template https://github.com/intellisyscorp/django-project-template/archive/master.zip \
    <<PROJECT_NAME>>
```

## Includes
- OWNERS 정보
- Swagger 연동
- v1 엔드포인트까지 자동 생성
- health check 엔드포인트까지 생성
