from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image=models.ImageField(upload_to="images/")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
