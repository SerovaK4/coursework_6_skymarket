from django.contrib import admin

from ads.models import Ad, Comment


# TODO здесь можно подкючить ваши модели к стандартной джанго-админке

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "description", "image", "author", "created_at")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("text", "created_at", "author", "ad")

