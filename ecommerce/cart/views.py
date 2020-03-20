from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from products.models import Product
from cart.models import Cart

def add_to_cart(request, slug):
	#with Cart model
	item = get_object_or_404(Product,slug=slug)  #product name on the basis of slug
	order_item, created = Cart.objects.get_or_create(     #order_item <-- (product name in cart)
		item=item,
		user=request.user
	)
	#with Order model
	order_qs = Order.objects.filter(user=request.user, ordered=False)  #order_qs <-- username for the unordered items
	if order_qs.exists():
		uzer = order_qs[0]
		if uzer.orderitems.filter(item__slug=item.slug).exists():
			order_item.qunatity+=1
			messages.info(request, "This item quantity is updated")
		else:
			uzer.orderitems.add(order_item)
			messages.info(request,"This item is added to your cart")
	else:
		Order.objects.create(user=request.user).add(orderitem=order_item)
		messages.info(request, "This item is added to your cart")
	return redirect ("mainapp:home")


def remove_from_cart(request, slug):
	item = get_object_or_404(Product,slug=slug)
	cart_qs = Cart.objects.filter(user=request.user, item=item)
	if cart_qs.exists():
		cart_qs.delete()
	else:
		messages.info("The iten was not in your cart")
	return redirect("mainapp:home")
	