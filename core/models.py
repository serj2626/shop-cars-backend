from django.db import models


class Seo(models.Model):
    """
    SEO Модель
    """

    url = models.CharField(max_length=255, verbose_name="Ссылка")
    og_image = models.CharField(
        max_length=255, verbose_name="Картинка для социальных сетей"
    )
    seo_title = models.CharField(
        max_length=255, verbose_name="Заголовок в результатах поиска"
    )
    seo_description = models.TextField(verbose_name="Описание в результатах поиска")
    og_title = models.CharField(
        max_length=255, verbose_name="Заголовок для социальных сетей"
    )
    og_description = models.TextField(verbose_name="Описание для социальных сетей")
    canonical = models.CharField(max_length=255, verbose_name="Каноническая ссылка")
    is_no_index = models.BooleanField(default=False, verbose_name="Нет индексации")
    is_no_follow = models.BooleanField(default=False, verbose_name="Нет следования")

    def __str__(self):
        return self.seo_title

    class Meta:
        verbose_name = "SEO"
        verbose_name_plural = "SEO"
