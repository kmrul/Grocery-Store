from django.db import models
from customer.models import Customer
from product.models import Product

class Order(models.Model):
    name = models.CharField(max_length=255)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    paid_amount = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    due_amount = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(editable=False, auto_now_add=True)
    update_date = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self):
        return self.name

class OrderLine(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    qty = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    cost_price = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(editable=False, auto_now_add=True)
    update_date = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self):
        return self.order_id.name + "-" + self.product_id.name