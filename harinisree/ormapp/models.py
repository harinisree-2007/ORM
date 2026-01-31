
from django.db import models
from django.contrib import admin
class Restaurantdb(models.Model):
    OrderID=models.IntegerField(primary_key=True);
    Name=models.CharField(max_length=15);
    mobileno=models.IntegerField();
    cuisine=models.CharField(max_length=100);
    location=models.CharField(max_length=500);
    rating=models.FloatField();
    is_open=models.CharField();
class RestaurantdbAdmin(admin.ModelAdmin):
    list_display=['OrderID','Name','mobileno','cuisine','location','rating','is_open'];

