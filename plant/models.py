from django.db import models
from django_resized import ResizedImageField
from django.contrib.auth.models import User

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
    
    # def __str__(self):
    #     return self.living_room
    
    
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
    user =  models.ForeignKey('auth.User', on_delete=models.PROTECT, related_name='plants')
    

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
    
# Create your models here.
