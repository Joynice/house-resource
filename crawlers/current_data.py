# -*- coding: UTF-8 -*-
__author__ = 'Joynice'
import requests
import math
import time
from models import LastData
from multiprocessing.dummy import Pool as ThreadPool
from common.mysql import mysql_db
from common.header import get_header
# from common.time import now_month, last_month, time_s
import datetime
session = mysql_db()
headers = get_header()


def getUrls(url):
    urlList = []
    data = requests.get(url=url.format(1), headers=headers).content.decode('unicode_escape')
    all = eval(data)['sums'].get('CNTALL')
    maxPage = math.ceil(int(all)/20)
    for i in range(1, maxPage+1):
        urlList.append(url.format(i))
    print(urlList)
    return urlList


def getData(url):
    dataList = []
    urlList = getUrls(url)
    for i in urlList:
        time.sleep(3)
        data = requests.get(url=i, headers=headers).content.decode('unicode_escape')
        print(i)
        dataList.append(data)
    return dataList


def saveData():
    '''
       #获得当月数据
       getData('http://zh.fzg360.com/wqzh/server.php?act=ajax&page={}&days=mnow&keyword=')
       #获得上月数据
       getData('http://zh.fzg360.com/wqzh/server.php?act=ajax&page={}&days=mprev&keyword=')
    '''
    urlList = ['http://zh.fzg360.com/wqzh/server.php?act=ajax&page={}&days=mnow&keyword=',
               'http://zh.fzg360.com/wqzh/server.php?act=ajax&page={}&days=mprev&keyword=']
    last_data = session.query(LastData).filter(LastData.month == str('{}.{}'.format(datetime.datetime.now().year, int((datetime.datetime.now().month))-1))).all()
    print(last_data)
    pool = ThreadPool(2)
    data = pool.map(getData, urlList)
    db1 = LastData(month='{}.{}'.format(datetime.datetime.now().year, datetime.datetime.now().month), data_list=str(data[0]))
    db2 = LastData(month='{}.{}'.format(datetime.datetime.now().year, int((datetime.datetime.now().month))-1), data_list=str(data[1]))
    session.add(db1)
    session.commit()
    if len(last_data) == 1:
        pass
    else:
        session.add(db2)
        session.commit()


def dropTableDate():
    try:
        all = session.query(LastData).filter(LastData.month == str('{}.{}'.format(datetime.datetime.now().year, datetime.datetime.now().month))).all()
        for i in all:
            session.delete(i)
        session.commit()
    except Exception as e:
        print(e)


def updateDate():
    while True:
        print('---------------{}开始更新------------------'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        dropTableDate()
        saveData()
        print('---------------{}更新完毕-------------------'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        time.sleep(900)

if __name__ == '__main__':
    updateDate()