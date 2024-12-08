from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.defaulttags import register
from django.views import View
from django.views.generic import ListView

from catalog_app.models import Item, Category, ItemImage


# Create your views here.
class HomeView(View):
    model = Item
    paginate_by = 5
    template_name = "home.html"

    def get(self, *args, **kwargs):
        items = Item.objects.all()
        categories = Category.objects.all()
        context = {
            'categories': categories,
            'items': items
        }
        return render(self.request, 'index.html', context)

class ItemListView(View):
    def get(self, *args, **kwargs):
        if self.kwargs.get('slug') is not None:
            category = Category.objects.filter(slug=self.kwargs['slug']).first()
            items = Item.objects.filter(category_id=category.pk)
        else:
            category = None
            items = Item.objects.all()
        all_categories = Category.objects.all().order_by("name")
        paginator = Paginator(items.order_by("name"), 8)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {
            'categories': all_categories,
            'active_category': category,
            'items': page_obj.object_list,
            'page_obj': page_obj
        }
        return render(self.request, 'index.html', context)

class ItemDetailsView(View):
    def get(self, *args, **kwargs):
        item = get_object_or_404(Item, sku = self.kwargs['sku'])
        category = Category.objects.filter(id = item.category_id).first()
        all_categories = Category.objects.all()
        images = ItemImage.objects.filter(item=item)
        context = {
            'categories': all_categories,
            'active_category': category,
            'item_details': item,
            "images": images
        }
        return render(self.request, 'index.html', context)