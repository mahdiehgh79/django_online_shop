from django.contrib import admin
from .models import Product, Comment


class CommentsInline(admin.TabularInline):
    model = Comment
    fields = ['stars', 'active', 'author', 'body', ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active',]

    inlines = [
        CommentsInline,
    ]


@admin.register(Comment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'stars', 'active', 'author', 'body', ]
