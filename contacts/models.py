from django.db import models
from common import vars


class Subscribe(models.Model):
    """
    Подписка на рассылку
    """

    email = models.EmailField("Почта", unique=True)

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

    def __str__(self):
        return f"Подписка: {self.email}"


class Feedback(models.Model):
    """
    Обратная связь
    """

    name = models.CharField("Имя", max_length=50)
    email = models.EmailField("Почта")
    phone = models.CharField("Телефон", max_length=50)
    subject = models.CharField(
        "Тема", max_length=50, choices=vars.SUBJECT, default="other"
    )
    message = models.TextField("Сообщение", max_length=2000)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
