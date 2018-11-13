# -*- coding: UTF-8 -*-
__author__ = 'Joynice'
import datetime
time_s = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
now_time = datetime.date.today()
now_month = '{}.{}'.format(datetime.datetime.now().year, datetime.datetime.now().month)
last_month = '{}.{}'.format(datetime.datetime.now().year, int((datetime.datetime.now().month))-1)