# How to use

Django project를 생성할 때 다음과 같이 입력할 경우 template대로 자동 생성됨.
``` bash
django-admin startproject \
    --template https://github.com/intellisyscorp/django-project-template/archive/master.zip \
    <<PROJECT_NAME>>
```

다음 커맨드를 실행해서 스크립트 파일들도 알맞게 변형 적용 가능
``` bash
# `<<PROJECT_NAME>>` 에 실제 프로젝트 명 기입
grep -rIl '{{ project_name }}' | xargs sed -i 's/{{ project_name }}/<<PROJECT_NAME>>/g'
```

## Includes
- OWNERS 정보
- Swagger 연동
- v1 엔드포인트까지 자동 생성
- health check 엔드포인트까지 생성
