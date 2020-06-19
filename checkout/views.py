from django.shortcuts import redirect, reverse
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.conf import settings

from products.models import Product
from .models import Order
from cart.context_processors import get_cart


class OrderCreateView(CreateView):
    model = Order
    fields = ['full_name', 'email', 'phone_number',
              'street_address1', 'street_address2',
              'town_or_city', 'postcode', 'country',
              'county', ]

    def dispatch(self, *args, **kwargs):
        cart = self.request.session.get('cart', {})
        if not cart:
            messages.error(self.request, "The cart is empty")
            return redirect(reverse('products:list'))
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_contents = get_cart(self.request)
        total = cart_contents['cart_total']
        cart_dict = self.request.session.get('cart', {})
        cart_list = []
        for key in cart_dict:
            cart_list.append(key)
        products = Product.objects.filter(id__in=cart_list)
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY

        order_form = context['form']

        context['stripe_public_key'] = stripe_public_key
        context['stripe_secret_key'] = stripe_secret_key
        context['products'] = products
        context['order_form'] = order_form
        return context
