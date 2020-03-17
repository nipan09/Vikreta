from django.shortcuts import render
from products.models import Product
from django.views.generic import ListView

class Home(ListView):
	model = Product
	template_name = 'home.html'

