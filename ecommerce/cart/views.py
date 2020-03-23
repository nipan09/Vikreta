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
	item = get_object_or_404(Product,slug=slug)  #product name on the basis of slug
	cart_qs = Cart.objects.filter(user=request.user, item=item)    #cart_qs <-- (product name in cart)
	if cart_qs.exists():
		cart = cart_qs[0]
		if cart.quantity>1:
			cart.quantity-=1
			cart.save()
		else:
			cart_qs.delete()
	order_qs = Order.objects.filter(user=request.user, ordered=False)    #removing the order as well 
	if order_qs.exists():
		uzer = order_qs[0]
		if uzer.orderitems.filter(item__slug=item.slug).exists():
			uzer.orderitems.remove((Cart.objects.filter(item=item, user=request.user))[0])
			messages.info(request,"This item has been removed from your cart")
		else:
			messages.info(request,"This item is not in your cart")
		return redirect("mainapp:home")
	else:
		messages.info(request,"You do not have an active order")
		return redirect("mainapp:home")


def cart_view():
	carts = Cart.objects.filter(user=request.user)
	orders = Order.objects.filter(user=request.user, filter=False)
	if carts.exists():
		order = orders[0]
		return render(request,'cart/cart.html',{'carts':carts, 'order':order})
	else:
		messages.warning(request, "Your cart is empty")
		return redirect()
		