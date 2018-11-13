# -*- coding: UTF-8 -*-
__author__ = 'Joynice'
import re
import random
import datetime
from models import ActualData
import requests
import time
from common.mysql import mysql_db
from common.header import get_header
from get_proxies.get_proxy import getProxy


proxies = getProxy(10)
session = mysql_db()
headers = get_header()
def getDate():
    try:
        date = requests.post('https://61.143.53.130:4433/zhpubweb/SaleCount3.aspx?readstate=ajax&type=7&year=2017&'
                             'month=8', verify=False, headers=headers, proxies={'http': random.choice(proxies)}).text
    except Exception as e:
        print(e)
    tagList = ['NAME', 'COUNT1', 'COUNT2', 'COUNT3', 'COUNT4']
    allList = []
    oneList = []
    # print(date)
    fin_List = []
    for i in tagList:
        dateList = re.findall(r'<{}>(.*?)</{}>'.format(i, i), date)
        allList.append(dateList)
    for i in range(len(dateList)):
        a = allList[0][i]
        b = allList[1][i]
        c = allList[2][i]
        d = allList[3][i]
        e = allList[4][i]
        lista = [a, b, c, d, e]
        fin_List.append(lista)
    house_resouce = ActualData(datatime=str(datetime.date.today()), data_list=str(fin_List))
    oneList.append(house_resouce)
    g = int(b)+int(c)+int(d)+int(e)
    print(g)
    return oneList, g


def saveDate():
    dateList = getDate()[0]
    for i in dateList:
        session.add(i)
    session.commit()


def dropTableDate():
    try:
        all = session.query(ActualData).filter(ActualData.datatime == str(datetime.date.today())).all()
        for i in all:
            session.delete(i)
        session.commit()
    except Exception as e:
        print(e)


def checkUpdate():
    while True:
        print('---------------{}开始更新------------------'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        date = session.query(ActualData).filter(ActualData.datatime == str(datetime.date.today())).first()
        print(date)
        if date == None:
            saveDate()
        else:
            date_list = eval(date.data_list)[-1]
            all_num = int(date_list[1]) + int(date_list[2]) + int(date_list[3]) + int(date_list[4])
            print(all_num)
            all_num_net = getDate()[1]
            if all_num != all_num_net:
                dropTableDate()
                saveDate()
            else:
                pass
        print('------------------{}更新完毕-------------------'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        time.sleep(900)


if __name__ == '__main__':
    # dropTableDate()
    # saveDate()
    # checkUpdate()
    # getDate()
    # dropTableDate()
    # saveDate()
    checkUpdate()
