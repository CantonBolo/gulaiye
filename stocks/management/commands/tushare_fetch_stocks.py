from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from stocks.models import Stock
import tushare as ts
import pandas as pd


class Command(BaseCommand):
    help = 'Fetch stocks base information from tushare pro api'

    def handle(self, *args, **options):
        pro = ts.pro_api(settings.TUSHARE_TOKEN)
        stocks = pro.query('stock_basic', exchange='', list_status='L',
                           fields='ts_code, symbol, name, area, industry, '
                                  'fullname, enname, market, exchange, '
                                  'curr_type, list_status, list_date, '
                                  'delist_date, is_hs')
        for index, stock in stocks.iterrows():
            print(index)
            print(stock.to_dict())
            Stock.objects.update_or_create(ts_code=stock.ts_code, defaults=stock.to_dict())
        stocks = pro.query('stock_basic', exchange='', list_status='D',
                           fields='ts_code, symbol, name, area, industry, '
                                  'fullname, enname, market, exchange, '
                                  'curr_type, list_status, list_date, '
                                  'delist_date, is_hs')
        for index, stock in stocks.iterrows():
            print(index)
            print(stock.to_dict())
            Stock.objects.update_or_create(ts_code=stock.ts_code, defaults=stock.to_dict())
        stocks = pro.query('stock_basic', exchange='', list_status='P',
                           fields='ts_code, symbol, name, area, industry, '
                                  'fullname, enname, market, exchange, '
                                  'curr_type, list_status, list_date, '
                                  'delist_date, is_hs')
        for index, stock in stocks.iterrows():
            print(index)
            print(stock.to_dict())
            Stock.objects.update_or_create(ts_code=stock.ts_code, defaults=stock.to_dict())
