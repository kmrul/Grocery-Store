from django.db import models
from django.contrib.auth.models import User
from category.models import Category

class Product(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=550)
    public_price = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    cost_price = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    update_date = models.DateTimeField(auto_now=True, editable=False)
    

    def __str__(self):
        return self.name