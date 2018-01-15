from django.contrib import admin

from .models import Item, Favorites, Purchase


class ItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(Item, ItemAdmin)
