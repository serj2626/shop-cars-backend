from django.db import models
import uuid
from cars.models import Car


class Order(models.Model):
    """
    Модель заказа
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField("Почта")
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    car = models.ForeignKey(
        Car, on_delete=models.SET_NULL, null=True, verbose_name="Машина"
    )
    prepayment = models.BooleanField("Предоплата", default=False)
    payment = models.BooleanField("Оплата", default=False)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ: {self.name} - {self.car}"


class Prepayment(models.Model):
    """
    Модель предоплаты
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, verbose_name="Заказ",
        related_name="prepayments"
    )
    sum = models.PositiveIntegerField("Сумма предоплаты", blank=True, null=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    def clean(self):
        if self.order.car.total_sum < 2000:
            self.sum = (10 / 100) * self.order.car.total_sum
        if self.order.car.total_sum < 3000:
            self.sum = (15 / 100) * self.order.car.total_sum
        else:
            self.sum = (20 / 100) * self.order.car.total_sum
        return super().clean()

    class Meta:
        verbose_name = "Предоплата"
        verbose_name_plural = "Предоплаты"

    def __str__(self):
        return f"Предоплата: {self.order}"


class Payment(models.Model):
    """
    Модель оплаты
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, null=True, verbose_name="Заказ",
        related_name="payments"
    )
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"

    def __str__(self):
        return f"Оплата: {self.order}"
