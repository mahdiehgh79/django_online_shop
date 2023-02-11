from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    image = models.ImageField(verbose_name=_('product_image'),upload_to='product/product_cover/', blank=True,)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])
class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', 'very bad'),
        ('2', 'bad'),
        ('3', 'Normal'),
        ('4', 'Good'),
        ('5', 'Perfect'),

    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments',)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments',)
    body = models.TextField(verbose_name='comment text')
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS, verbose_name='what is your score ?')
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = models.Manager()
    active_comments_manager = ActiveCommentsManager()

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])


