from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(editable=False, auto_now_add=True)
    update_date = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self):
        return self.name