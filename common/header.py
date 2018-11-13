# -*- coding: UTF-8 -*-
__author__ = 'Joynice'
from fake_useragent import UserAgent

def get_header():
    ua = UserAgent().random
    headers = {'User-Agent': ua}
    return headers