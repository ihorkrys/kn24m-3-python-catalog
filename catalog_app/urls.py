"""
URL configuration for cursova project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from catalog_app import views

app_name = 'catalog_app'

urlpatterns = [
    path('', views.ItemListView.as_view(), name='home'),
    path('category/<slug>', views.ItemListView.as_view(), name='category_items'),
    path('item/<sku>', views.ItemDetailsView.as_view(), name='item'),
]
