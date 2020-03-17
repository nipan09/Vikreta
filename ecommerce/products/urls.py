from django.urls import path
from products.views import Home
from cart import views

app_name= 'mainapp' 

urlpatterns=[
		path('',Home.as_view(), name='home'),
		path('cart/<slug>',views.add_to_cart, name='cart'),
		path('remove/<slug>',views.remove_from_cart, name='remove-cart'),
	]