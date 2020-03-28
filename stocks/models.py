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
    list_date = models.DateField(null=True, blank=True)
    delist_date = models.DateField(null=True, blank=True)
    is_hs = models.CharField(max_length=1, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class NameChange(models.Model):
    stock = models.ForeignKey(to=Stock, to_field='ts_code', on_delete=models.CASCADE)
    name = models.CharField(max_length=36)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    ann_date = models.DateField(null=True, blank=True)
    change_reason = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


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
    employees = models.IntegerField(null=True, blank=True)
    main_business = models.TextField(null=True, blank=True)
    business_scope = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class HsConst(models.Model):
    stock = models.ForeignKey(to=Stock, to_field='ts_code', on_delete=models.CASCADE)
    hs_type = models.CharField(max_length=2)
    in_date = models.DateField(null=True, blank=True)
    out_date = models.DateField(null=True, blank=True)
    is_new = models.BooleanField(null=True, blank=True)


class DailyBasic(models.Model):
    stock = models.ForeignKey(to=Stock, to_field='ts_code', on_delete=models.CASCADE)
    trade_date = models.DateField(max_length=10, null=True, blank=True, db_index=True)
    close = models.FloatField(null=True, blank=True)
    turnover_rate = models.FloatField(null=True, blank=True)
    turnover_rate_f = models.FloatField(null=True, blank=True)
    volume_ratio = models.FloatField(null=True, blank=True)
    pe = models.FloatField(null=True, blank=True)
    pe_ttm = models.FloatField(null=True, blank=True)
    pb = models.FloatField(null=True, blank=True)
    ps = models.FloatField(null=True, blank=True)
    ps_ttm = models.FloatField(null=True, blank=True)
    dv_ratio = models.FloatField(null=True, blank=True)
    dv_ttm = models.FloatField(null=True, blank=True)
    total_share = models.FloatField(null=True, blank=True)
    float_share = models.FloatField(null=True, blank=True)
    free_share = models.FloatField(null=True, blank=True)
    total_mv = models.FloatField(null=True, blank=True)
    circ_mv = models.FloatField(null=True, blank=True)


class AdjFactor(models.Model):
    stock = models.ForeignKey(to=Stock, to_field='ts_code', on_delete=models.CASCADE)
    trade_date = models.DateField(null=True, blank=True, db_index=True)
    adj_factor = models.FloatField(null=True, blank=True)


class LimitList(models.Model):
    stock = models.ForeignKey(to=Stock, to_field='ts_code', on_delete=models.CASCADE)
    trade_date = models.DateField(null=True, blank=True, db_index=True)
    name = models.CharField(max_length=36)
    close = models.FloatField(null=True, blank=True)
    pct_chg = models.FloatField(null=True, blank=True)
    amp = models.FloatField(null=True, blank=True)
    fc_ratio = models.FloatField(null=True, blank=True)
    fl_ratio = models.FloatField(null=True, blank=True)
    fd_amount = models.FloatField(null=True, blank=True)
    first_time = models.TimeField(null=True, blank=True)
    last_time = models.TimeField(null=True, blank=True)
    open_times = models.IntegerField(null=True, blank=True, default=0)
    strth = models.FloatField(null=True, blank=True)
    limit = models.CharField(max_length=1, null=True, blank=True)
