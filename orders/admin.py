from django.contrib import admin
from .models import Order, Payment, Prepayment


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Админка заказов
    """

    list_display = (
        "name",
        "email",
        "phone",
        "car",
        "prepayment",
        "payment",
        "created_at",
    )


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """
    Админка оплаты
    """

    list_display = (
        "order",
        "created_at",
        "updated_at",
    )


@admin.register(Prepayment)
class PrepaymentAdmin(admin.ModelAdmin):
    """
    Админка предоплаты
    """

    list_display = (
        "order",
        "sum",
        "created_at",
        "updated_at",
    )
