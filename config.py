# -*- coding: UTF-8 -*-
__author__ = 'Joynice'
import os
import pymysql
DEBUG = True
SECRET_KEY = os.urandom(24)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:120.79.51.146/hr?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False