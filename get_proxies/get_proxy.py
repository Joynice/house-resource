# -*- coding: UTF-8 -*-
__author__ = 'Joynice'
import requests


def getProxy(num):

    url = 'http://dev.kdlapi.com/api/getproxy/?orderid=969422369394878&num={}&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=1&method=2&an_an=1&an_ha=1&sp1=1&sp2=1&quality=1&sort=1&format=json&sep=1'.format(num)
    Proxy_dict = requests.get(url=url).json()
    Proxy_list = Proxy_dict.get('data').get('proxy_list')
    return Proxy_list
