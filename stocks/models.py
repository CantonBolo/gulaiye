from django.db import models

class Stock(models.Model):
    ts_code = models.TextField(max_length=9)
    symbol = models.TextField(max_length=6)
    name = models.TextField(max_length=36)
    area = models.TextField(max_length=36, null=True, blank=True)
    industry = models.TextField(max_length=36, null=True, blank=True)
    fullname = models.TextField(max_length=256, null=True, blank=True)
    enname = models.TextField(max_length=256, null=True, blank=True)
    market = models.TextField(max_length=18, null=True, blank=True)
    exchange = models.TextField(max_length=18, null=True, blank=True)
    curr_type = models.TextField(max_length=18, null=True, blank=True)
    list_status = models.TextField(max_length=1, null=True, blank=True)
    list_date = models.TextField(max_length=8, null=True, blank=True)
    delist_date = models.TextField(max_length=8, null=True, blank=True)
    is_hs = models.CharField(max_length=1, null=True, blank=True)
