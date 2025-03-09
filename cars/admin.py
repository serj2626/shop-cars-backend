from django.contrib import admin
from .models import Brand, ModelCar, Car, Sale, Review, SaleCar


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Админка отзывов
    """

    list_display = (
        "car",
        "user",
        "stars",
    )


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    """
    Админка акций
    """

    list_display = ("descount",)


@admin.register(SaleCar)
class SaleCarAdmin(admin.ModelAdmin):
    """
    Админка акции машин
    """

    list_display = (
        "car",
        "sale",
    )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """
    Админка марок
    """

    list_display = ("title", "country", "slug")


@admin.register(ModelCar)
class ModelCarAdmin(admin.ModelAdmin):
    """
    Админка моделей
    """

    list_display = (
        "title",
        "brand",
        "slug",
    )

    list_editable = ("brand",)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    """
    Админка машин
    """

    list_display = (
        "model_car",
        "color",
        "transmission",
        "drive",
        "state",
        "mileage",
        "price",
        "sale",
    )

    list_editable = (
        "color",
        "transmission",
        "drive",
        "state",
        "mileage",
        "price",
        "sale",
    )
