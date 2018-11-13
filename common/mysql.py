# -*- coding: UTF-8 -*-
__author__ = 'Joynice'
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config


def mysql_db():
    engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
    dbsessin = sessionmaker(bind=engine)
    session = dbsessin()
    return session