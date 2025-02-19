from django.db import models
from django.contrib.auth.models import User

# Create your models here.

SUPPLIERS = (
    ('Supplier1', 'Supplier1'),
    ('Supplier2', 'Supplier2')
)

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}-{self.location}'

class Product(models.Model):
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name}'

class Assembly(models.Model):
    name=models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='assemblies')

    def __str__(self):
        return f'{self.name}'


class Component(models.Model):
    description = models.CharField(max_length=255)
    specification = models.CharField(max_length=255)
    supplier = models.CharField(max_length=50, choices=SUPPLIERS)
    make = models.CharField(max_length=255)
    package_size = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    uom = models.CharField(max_length=50)
    identity = models.CharField(max_length=50)
    tol_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    inventory_qty=models.PositiveIntegerField()
    assembly = models.ForeignKey(Assembly, on_delete=models.CASCADE, null=True, related_name='components')

    def __str__(self):
        return f'{self.description}-{self.inventory_qty}'


class Order(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.customer}-{self.name}'