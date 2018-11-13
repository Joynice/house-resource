# -*- coding: UTF-8 -*-
__author__ = 'Joynice'
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from exts import db
from app import app
from models import ActualData, LastData
from config import SQLALCHEMY_DATABASE_URI
manager = Manager(app)

#使用Migrate 绑定app,db
migrate = Migrate(app, db)

#添加迁移脚本命令到manager中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()