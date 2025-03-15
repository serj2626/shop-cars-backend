from django.db import models
import uuid
from common import vars, functions
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.timesince import timesince


class Sale(models.Model):
    """
    Модель типы акций
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    discount = models.IntegerField("Скидка", null=True, blank=True)
    description = CKEditor5Field(
        blank=True, verbose_name="Условия", config_name="extends"
    )

    class Meta:
        verbose_name = "Типы акций"
        verbose_name_plural = "Типы акций"

    def __str__(self):
        return f"Акция: скидка {self.discount}%"


class Brand(models.Model):
    """
    Модель марки
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Название марки", max_length=50, unique=True)
    country = models.CharField(
        "Страна", max_length=50, null=True, blank=True, choices=vars.COUNTRIES
    )
    image = models.ImageField(
        "Значок", upload_to=functions.get_path_for_avatar_brand, null=True, blank=True
    )
    description = CKEditor5Field(
        blank=True, verbose_name="Описание", config_name="extends"
    )
    slug = models.SlugField("Слаг", max_length=50, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Марка"
        verbose_name_plural = "Марки"

    def __str__(self):
        return f"Бренд: {self.title}"


class ModelCar(models.Model):
    """
    Модель автомобиля
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Марка")
    title = models.CharField("Название модели", max_length=50, unique=True)
    slug = models.SlugField("Слаг", max_length=50, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"

    def __str__(self):
        return f"{self.brand.title} {self.title}"


class Car(models.Model):
    """
    Модель машины
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model_car = models.ForeignKey(
        ModelCar, on_delete=models.CASCADE, verbose_name="Модель"
    )
    body = models.CharField(
        "Тип кузова", max_length=50, choices=vars.BODY, default="sedan"
    )
    year = models.IntegerField("Год", null=True, blank=True)
    color = models.CharField(
        "Цвет", max_length=50, choices=vars.COLORS, default="black"
    )
    transmission = models.CharField(
        "Трансмиссия", max_length=50, choices=vars.TRANSMISSION, default="auto"
    )
    drive = models.CharField(
        "Привод", max_length=50, choices=vars.DRIVE, default="front"
    )
    state = models.CharField(
        "Состояние", max_length=50, choices=vars.STATE, default="new"
    )
    mileage = models.IntegerField("Пробег", null=True, blank=True)
    price = models.IntegerField("Цена", null=True, blank=True)
    sale = models.BooleanField("Акция", default=False)
    total_sum = models.IntegerField("Итоговая цена", null=True, blank=True)
    image = models.ImageField(
        "Значок", upload_to=functions.get_path_for_avatar_car, null=True, blank=True
    )
    description = CKEditor5Field(
        blank=True, verbose_name="Описание", config_name="extends"
    )

    @property
    def articul(self):
        return f"арт-{str(self.id).lower().replace('-', '')}"


    def clean(self):
        if not self.sale:
            self.total_sum = self.price
        else:
            self.total_sum = self.price - self.price * self.sale.discount / 100
        return super().clean()

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"

    def __str__(self):
        return f"Машина: {self.model_car.brand.title} {self.model_car.title}"


class ImageCar(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    car = models.ForeignKey(
        Car, on_delete=models.CASCADE, verbose_name="Машина", related_name="images"
    )
    image = models.ImageField(
        "Фото",
        upload_to=functions.get_path_for_all_images_by_car,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return f"Изображение: {self.car}"


class SaleCar(models.Model):
    """
    Модель акции
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Машина")
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, verbose_name="Акция")

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"

    def __str__(self):
        return f"Акция: {self.car}"


class Review(models.Model):
    """
    Модель отзыва
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Машина")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    comment = models.TextField("Текст", max_length=2000)
    stars = models.SmallIntegerField(
        "Оценка", validators=[MinValueValidator(1), MaxValueValidator(5)], default=5
    )
    verified = models.BooleanField("Проверен", default=False)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    def time_ago(self):
        return timesince(self.created_at)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"Отзыв: {self.car}"
