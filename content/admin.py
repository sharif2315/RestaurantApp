from django.contrib import admin

from .models import MenuCategory, MenuItem
from django.db.models import Count


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'total_menu_items']
    list_filter = ['name']
    search_fields = ['name']
    ordering = ['name', 'order']

    def get_queryset(self, request):
        # Annotate with the count of menu items
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            total_items_count=Count('menuitem')
        )
        return queryset

    def total_menu_items(self, obj):
        return obj.total_items_count
    total_menu_items.admin_order_field = 'total_items_count'  # Enables ordering by this custom column
    total_menu_items.short_description = 'Total Items'

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']
    list_filter = ['category']
    autocomplete_fields = ['category']
