from django.db import models

# Create your models here.
class CategoryModule(models.Model):
    name = models.CharField(max_length = 6)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class ProductModule(models.Model):
    category = models.ForeignKey(CategoryModule, on_delete = models.CASCADE)
    title = models.CharField(max_length = 20)
    pCategory = models.CharField(max_length = 20)
    price = models.IntegerField()
    brand = models.CharField(max_length = 10)
    reward_points = models.IntegerField()
    description = models.TextField()
    size = models.TextField()
    color = models.TextField()
    image = models.ImageField(upload_to='Products')

    class Meta:
        verbose_name_plural = 'Products'
        
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'Contacts'
        
    def __str__(self):
        return self.name