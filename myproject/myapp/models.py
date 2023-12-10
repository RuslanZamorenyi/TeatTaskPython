from django.db import models

# Create your models here.


class CostsModel(models.Model):
    location = models.CharField(max_length=50)
    channel = models.CharField(max_length=50)
    medium = models.CharField(max_length=50)
    campaign = models.CharField(max_length=50)
    keyword = models.CharField(max_length=50)
    ad_content = models.CharField(max_length=50)
    ad_group = models.CharField(max_length=50)
    landing_page = models.CharField(max_length=50)


class Orders(models.Model):
    user_id = models.IntegerField()
    orders = models.CharField(max_length=50)