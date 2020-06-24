from django.shortcuts import redirect, reverse
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.contrib.postgres.search import (SearchQuery,
                                            SearchRank,
                                            SearchVector)

from .models import Product, StockDrop


class ProductListView(ListView):
    """Renders the home page with a Products List."""
    model = Product
    context_object_name = 'products'
    ordering = ['-date_added']

    def get_queryset(self):
        if 'query' in self.request.GET:
            if self.request.GET['query'] == '':
                messages.warning(self.request,
                                 "You didn't search for anything")
                return Product.objects.all()
            self.user_query = self.request.GET['query']
            self.vector = SearchVector('name', 'description', weight='A') + \
                SearchVector('admin_tags', 'user_tags', weight='B')
            self.query = SearchQuery(self.user_query)
            self.rank = SearchRank(self.vector, self.query)
            return Product.objects.annotate(rank=self.rank).order_by('-rank')\
                .filter(rank__gt=0)

        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.GET:
            stockdrops = StockDrop.objects.filter(display=True)
            context['stockdrops'] = stockdrops

        products_active = True

        context['products_active'] = products_active
        return context


class ProductDetailView(DetailView):
    """Renders the product detail page"""
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories_active = True
        context['categories_active'] = categories_active
        return context


class StockDropDetailView(DetailView):
    """Renders the home page with a Products List."""
    model = StockDrop
    context_object_name = 'stockdrop'
