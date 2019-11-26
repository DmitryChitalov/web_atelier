from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя категории', max_length=128, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='активность', default=True)

    def __str__(self):
        # return f'{self.name}'
        return f'ProductCategory: {self.name} ({self.pk})'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory,
                                 verbose_name='категория',
                                 on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    short_desc = models.CharField(verbose_name='краткое описание', max_length=512, blank=True)
    characteristic = models.TextField(verbose_name='характеристики товара', blank=True)
    description = models.TextField(verbose_name='подробное описание', blank=True)
    quantity = models.PositiveIntegerField(verbose_name='на складе', default=0)
    is_active = models.BooleanField(verbose_name='активность', default=True)

    def __str__(self):
        # return f'{self.name} ({self.category.name})'
        return f'{self.category.name}: {self.name}'

    @staticmethod
    def get_items():
        return Product.objects.filter(is_active=True).order_by('category__name', 'name')