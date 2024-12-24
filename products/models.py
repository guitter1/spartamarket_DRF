from django.db import models
from django.conf import settings


class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image=models.ImageField(upload_to="images/")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  related_name="products")
