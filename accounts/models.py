from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank = True, on_delete= models.CASCADE)
    name = models.CharField(max_length = 200, null = True)
    phone = models.CharField(max_length = 100, null = True)
    email = models.EmailField(max_length = 200, null = True)
    profile_pic = models.ImageField(default = "default.jpg", null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    name = models.CharField(max_length = 200, null = True)
    price = models.DecimalField(decimal_places = 2, max_digits = 19, null = True)
    category = models.CharField(max_length = 200, null = True, choices = CATEGORY)
    description = models.CharField(max_length = 200, null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    # one to many relatioship between customer and orders
    # one customer can have many orders but one order can only be referenced to one customer
    customer = models.ForeignKey(Customer, null = True, on_delete= models.SET_NULL)
    product = models.ForeignKey(Product, null= True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add= True, null = True)
    status = models.CharField(max_length = 200, null = True, choices = STATUS)
    

    def __str__(self):
        return f'Ordered By {self.customer} for {self.product}'