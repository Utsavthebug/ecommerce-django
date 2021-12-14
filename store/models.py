from django.db import models
from category.models import Category
from django.urls import reverse

class Product(models.Model):
    product_name=models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    description = models.TextField(max_length=500,unique=True)
    price=models.IntegerField(default=0)
    images = models.ImageField(upload_to='photos/products')
    is_available = models.BooleanField(default=True)
    stock = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date= models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_details',kwargs={'category_slug':self.category.slug,'product_slug':self.slug})


    def __str__(self):
        return self.product_name







