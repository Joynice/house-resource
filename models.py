# -*- coding: UTF-8 -*-
__author__ = 'Joynice'
from exts import db


class ActualData(db.Model):
    __tablename__ = 'actual_data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    datatime = db.Column(db.String(100), nullable=False)
    data_list = db.Column(db.Text, nullable=False)


class LastData(db.Model):
    __tablename__ = 'last_data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    month = db.Column(db.String(15), nullable=False)
    data_list = db.Column(db.Text, nullable=False)
