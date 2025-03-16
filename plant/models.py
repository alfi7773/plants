from django.db import models
from django_resized import ResizedImageField
from django.contrib.auth.models import User
from django.db.models import Avg
from django_countries.fields import CountryField
from django.contrib.auth.models import AbstractUser


class TimeAbstract(models.Model):
    
    created_at = models.DateField('created', auto_now_add=True)
    updated_at = models.DateField('', auto_now=True)
    
    class Meta:
        abstract = True
        
class Category(TimeAbstract):
    
    class Meta:
        verbose_name_plural = 'categories'
        verbose_name = 'category'
        
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

    
class Size(TimeAbstract):
    
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
        
    TYPES = [
        (SMALL,'small'),
        (MEDIUM, 'medium'),
        (LARGE, 'large')
    ]
    
    class Meta:
        verbose_name_plural = 'sizes'
        verbose_name = 'size'
        
    name = models.CharField(max_length=100)
    type = models.CharField(choices=TYPES, default=SMALL, max_length=50)
    
    def __str__(self):
        return self.name


class Tag(TimeAbstract):
    
    class Meta:
        verbose_name_plural = 'tags'
        verbose_name = 'tag'
        
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Description(TimeAbstract):
    
    class Meta:
        verbose_name_plural = 'descriptions'
        verbose_name = 'description'
    
    living_room = models.TextField()
    dinig_room = models.TextField()
    ofice = models.TextField()
    
    def __str__(self):
        return f'{self.living_room}, {self.dinig_room}, {self.ofice}'
    
    

class Rating(TimeAbstract):
    
    class Meta:
        verbose_name_plural = 'ratings'
        verbose_name = 'rating'
    
    plant = models.ForeignKey('plant.Plant', on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f'{self.user} - {self.plant} ({self.score})'


# class CustomUser(AbstractUser):
#     STATUS_CHOICES = [
#         ('salesman', 'Salesman'),
#         ('buyer', 'Buyer')
#     ]
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='buyer')



class MyProfile(models.Model):
    STATUS_CHOICES = [
        ('seller', 'Salesman'),
        ('buyer', 'Buyer'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)


    def __str__(self):
        return f"{self.user.username} - {self.get_status_display()}"

    
class Plant(TimeAbstract):
    
    class Meta:
        verbose_name_plural = 'plants'
        verbose_name = 'plant'
        
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    short_description = models.TextField()
    sizes = models.ManyToManyField('plant.Size', related_name='plant')
    category = models.ForeignKey('plant.Category', on_delete=models.PROTECT, related_name='plant')
    tags = models.ManyToManyField('plant.Tag', related_name='plant')
    description = models.ForeignKey('plant.Description', on_delete=models.PROTECT)
    user =  models.ForeignKey(User, on_delete=models.PROTECT, related_name='plants', default=1)
    

    @property
    def image(self):
        if self.images.first():
            return self.images.first().image
        return None
    

    
    def __str__(self):
        return self.name

class ImagePlant(TimeAbstract):
    
    class Meta:
        verbose_name_plural = 'images'
        verbose_name = 'image'
        
    plant = models.ForeignKey('plant.Plant', on_delete=models.PROTECT, related_name='images')
    image = ResizedImageField(upload_to='plant_images/', quality=90, force_format='WEBP')
    
    
class Blog(TimeAbstract):
    
    class Meta:
        verbose_name_plural = 'blogs'
        verbose_name = 'blog'
        
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    
    def __str__(self):
        return self.name

class Cart(TimeAbstract):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    plant = models.ManyToManyField('plant.Plant', through='CartItem')

    def get_total(self):
        return sum(item.get_total() for item in self.cart_items.all())

class CartItem(TimeAbstract):
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.PROTECT)
    plant = models.ForeignKey('plant.Plant', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)

    def get_total(self):
        return self.plant.price * self.quantity

class Region(models.Model):
    
    first_name = models.CharField('first_name', max_length=100)
    last_name = models.CharField('first_name', max_length=100)
    country = CountryField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.country.name})"
    

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"{self.plant.name} - {self.quantity} pcs"

    def get_total(self):
        return self.price * self.quantity
    
# Create your models here.
