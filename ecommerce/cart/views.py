from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from cart.models import Cart

def add_to_cart(request, slug):
	item = get_object_or_404(Product,slug=slug)
	order_item, created = Cart.objects.get_or_create(
		item=item,
		user=request.user
	)
	return redirect("mainapp:home")

def remove_from_cart(request, slug):
	item = get_object_or_404(Product,slug=slug)
	cart_qs = Cart.objects.filter(user=request.user, item=item)
	if cart_qs.exists():
		cart_qs.delete()
	else:
		messages.info("The iten was not in your cart")
	return redirect("mainapp:home")