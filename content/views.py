from django.shortcuts import render

from .models import MenuCategory, MenuItem


def home(request):
    # Get all menu categories
    menu_categories = MenuCategory.objects.all()

    # For each category, fetch its associated menu items
    for category in menu_categories:
        category.menu_items = MenuItem.objects.filter(category=category)

    # Pass the menu categories with items to the template
    context = {"menu_categories": menu_categories}
    return render(request, "home.html", context)
