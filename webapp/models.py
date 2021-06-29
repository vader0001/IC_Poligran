from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=40, unique=True)
    address = models.CharField(max_length=70)
    city = models.CharField(max_length=100)
    department = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Customer  , self).save(*args, **kwargs)

    def __str__(self):
        return self.email

class ItemCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    
class Item(models.Model):

    class ItemType(models.TextChoices):
        PRODUCT = 'product', 'Producto'
        SERVICE = 'service', 'Service'

    name = models.CharField(max_length=50)
    sku = models.CharField(max_length=25)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    discount = models.IntegerField()
    stock = models.IntegerField()
    weight = models.IntegerField()
    Item_type = models.CharField(
        max_length=12,
        choices=ItemType.choices,
        default=ItemType.PRODUCT,
    )
    categoria = models.ForeignKey(ItemCategory,blank=True,default=None, on_delete = models.CASCADE) 
    photo = models.ImageField(upload_to='webapp/static/images', default='')

    def __str__(self):
        return self.name

    def photo_name(self):
        return self.photo.name.replace('webapp', '') 

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.item.name

class Order(models.Model):
    class OrderStatus(models.TextChoices):
        APPROVED = 'delivered', 'Entregado'
        PREPARING = 'preparing', 'En preparación'

    customer = models.ForeignKey(User,blank=True,default=None, on_delete = models.CASCADE)
    room_number =  models.CharField(max_length=10)
    item = models.ForeignKey(OrderItem,blank=True,default=None, on_delete = models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=OrderStatus.choices,
        default=OrderStatus.PREPARING,
    )

    def __str__(self):
        return self.customer.email + ' - ' + self.room_number

    def getStatus(self):
        if self.status == 'delivered':
            return 'Entregado'
        if self.status == 'preparing':
            return 'En preparación'