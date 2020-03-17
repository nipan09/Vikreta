from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product

User = get_user_model()

class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	item = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.quantity} of {self.item.name}'

class Order(models.Model):
	ordered = models.BooleanField(default=False)
	orderitems = models.ManyToManyField(Cart)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.username