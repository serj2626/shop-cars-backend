from django.contrib import admin
from .models import Feedback, Subscribe


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """
    Админка обратной связи
    """

    list_display = (
        "name",
        "email",
        "phone",
        "subject",
    )

@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    '''
    Админка подписки
    '''

    list_display = ('email',)