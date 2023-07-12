from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    order_number = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=100)
    quantity_ordered = models.IntegerField()
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.order_number}"

class Inventory(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    product_name = models.CharField(max_length=100)
    quantity_in_stock = models.IntegerField()
    quantity_in_input = models.IntegerField()

    def __str__(self):
        return f"Inventory {self.product_name}"

class Schedule(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    product_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Schedule {self.product_name}"

class Quality(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    product_name = models.CharField(max_length=100)
    quality_status = models.CharField(max_length=20)
    quality_issue = models.CharField(max_length=50)

    def __str__(self):
        return f"Quality {self.product_name}"
