from django.contrib import admin

# Register your models here.
from .models import Category, ItemImage
from .models import Item


admin.site.register(Category)

class ItemImageAdmin(admin.StackedInline):
    model = ItemImage

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageAdmin]

    class Meta:
       model = Item

@admin.register(ItemImage)
class ItemImageAdmin(admin.ModelAdmin):
    pass