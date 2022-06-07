from operator import truediv
from django.db import models

# Create your models here.

class categoryWarehouse(models.Model):

    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

class warehouse(models.Model):

    description = models.CharField(max_length=200)
    category = models.ForeignKey(categoryWarehouse, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.description