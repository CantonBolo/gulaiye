from django.db import models


class Stock(models.Model):
    ts_code = models.CharField(max_length=9, unique=True, primary_key=True)
    symbol = models.CharField(max_length=6, db_index=True)
    name = models.CharField(max_length=36)
    area = models.CharField(max_length=36, null=True, blank=True)
    industry = models.CharField(max_length=36, null=True, blank=True)
    fullname = models.CharField(max_length=256, null=True, blank=True)
    enname = models.CharField(max_length=256, null=True, blank=True)
    market = models.CharField(max_length=18, null=True, blank=True)
    exchange = models.CharField(max_length=18, null=True, blank=True)
    curr_type = models.CharField(max_length=18, null=True, blank=True)
    list_status = models.CharField(max_length=1, null=True, blank=True)
    list_date = models.DateField(max_length=8, null=True, blank=True)
    delist_date = models.DateField(max_length=8, null=True, blank=True)
    is_hs = models.CharField(max_length=1, null=True, blank=True)


class NameChange(models.Model):
    stock = models.ForeignKey(to=Stock, to_field='ts_code', on_delete=models.CASCADE)
    name = models.CharField(max_length=36)
    start_date = models.DateField(max_length=8, null=True, blank=True)
    end_date = models.DateField(max_length=8, null=True, blank=True)
    ann_date = models.DateField(max_length=8, null=True, blank=True)
    change_reason = models.TextField(null=True, blank=True)


class Company(models.Model):
    stock = models.OneToOneField(to=Stock, on_delete=models.CASCADE, primary_key=True)
    exchange = models.CharField(max_length=18, null=True, blank=True)
    chairman = models.CharField(max_length=36, null=True, blank=True)
    manager = models.CharField(max_length=36, null=True, blank=True)
    secretary = models.CharField(max_length=36, null=True, blank=True)
    reg_capital = models.FloatField()
    setup_date = models.DateField(max_length=8, null=True, blank=True)
    province = models.CharField(max_length=36, null=True, blank=True)
    city = models.CharField(max_length=36, null=True, blank=True)
    introduction = models.TextField(null=True, blank=True)
    website = models.CharField(max_length=256, null=True, blank=True)
    email = models.CharField(max_length=256, null=True, blank=True)
    office = models.CharField(max_length=256, null=True, blank=True)
    employees = models.IntegerField()
    main_business = models.CharField(max_length=256, null=True, blank=True)
    business_scope = models.CharField(max_length=256, null=True, blank=True)
