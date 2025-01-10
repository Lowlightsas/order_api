from django.db import models


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending','Pending'),
        ('confirmed','Confirmed'),
        ('cancelled','Cancelled'),
    ]

    order_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='pending')
    total_price = models.DecimalField(max_digits=10,decimal_places=2)
    products = models.ManyToManyField(Product,related_name='orders')
    is_deleted = models.BooleanField(default=False) # для мягкого удаления 

    def __str__(self):
        return f'Order {self.order_id} - {self.customer_name}'