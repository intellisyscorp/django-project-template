from django.db import models


class BaseModel(models.Model):

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
        verbose_name="생성 일시",
        help_text="데이터가 생성된 날짜입니다.",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=False,
        verbose_name="수정 일시",
        help_text="데이터가 수정된 날짜입니다.",
    )

    class Meta:
        abstract = True


class BaseActiveModel(models.Model):

    is_active = models.BooleanField(
        default=True,
        db_index=True,
        verbose_name="활성화 여부",
        help_text="활성화할지 여부를 결정합니다.",
    )

    class Meta:
        abstract = True


class BaseConfidenceModel(models.Model):

    confidence = models.FloatField(
        default=0.0,
        verbose_name="신뢰도",
        help_text="해당 정보의 신뢰도를 나타냅니다."
    )

    class Meta:
        abstract = True


class BaseNameModel(models.Model):

    name = models.CharField(
        max_length=40,
        primary_key=True,
        verbose_name="고유 명칭",
        help_text="고유 명칭을 나타냅니다.",
    )
    name_en = models.CharField(
        max_length=40,
        blank=True,
        null=True,
        verbose_name="영어 명칭",
        help_text="고유 영어 명칭을 나타냅니다.",
    )
    name_ko = models.CharField(
        max_length=40,
        blank=True,
        null=True,
        verbose_name="한국어 명칭",
        help_text="고유 한국어 명칭을 나타냅니다.",
    )

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        return self.name
