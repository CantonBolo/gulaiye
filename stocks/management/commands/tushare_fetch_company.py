from django.core.management.base import BaseCommand
from django.conf import settings
from datetime import datetime
from math import isnan
from stocks.models import Company, Stock
import tushare as ts
import pandas as pd


class Command(BaseCommand):
    help = 'Fetch stocks company information from tushare pro api'

    def handle(self, *args, **options):
        pro = ts.pro_api(settings.TUSHARE_TOKEN)
        stocks = Stock.objects.filter(company__isnull=True).all()[:5]
        companies = pro.query('stock_company', fields='ts_code, exchange, chairman, manager, secretary, reg_capital, setup_date, '
                                                      'province, city, introduction, website, email, office, employees, '
                                                      'main_business, business_scope')
        # print(companies)
        for index, company in companies.iterrows():
            try:
                stock = Stock.objects.get(ts_code=company.ts_code)
            except Stock.DoesNotExist:
                continue
            else:
                company.setup_date = datetime.strptime(company.setup_date, '%Y%m%d').date()
                company.reg_capital = '{:.2f}'.format(company.reg_capital)
                data = company.to_dict()
                del data['ts_code']
                if isnan(data['employees']):
                    data['employees'] = None
                print(data)
                Company.objects.update_or_create(stock=stock, defaults=data)
