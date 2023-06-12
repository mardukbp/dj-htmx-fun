# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'cost', 'status')
    search_fields = ('name',)
