from django.core.management.base import BaseCommand
from django.conf import settings
from datetime import datetime
from stocks.models import NameChange, Stock
import tushare as ts
import pandas as pd


class Command(BaseCommand):
    help = 'Fetch stocks name change from tushare pro api'

    def handle(self, *args, **options):
        pro = ts.pro_api(settings.TUSHARE_TOKEN)
        stocks = pro.query('namechange')
        for index, stock in stocks.iterrows():
            if stock.start_date is not None:
                stock.start_date = datetime.strptime(stock.start_date, '%Y%m%d').date()
            if stock.end_date is not None:
                stock.end_date = datetime.strptime(stock.end_date, '%Y%m%d').date()
            if stock.ann_date is not None:
                stock.ann_date = datetime.strptime(stock.ann_date, '%Y%m%d').date()
            data = stock.to_dict()
            # data['stock_id'] = data['ts_code']
            print(data)
            try:
                stockInfo = Stock.objects.get(ts_code=data['ts_code'])
            except Stock.DoesNotExist:
                continue
            else:
                del data['ts_code']
                # print(stockInfo)
                NameChange.objects.update_or_create(stock=stockInfo, start_date=data['start_date'], defaults=data)
