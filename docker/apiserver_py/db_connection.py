# !/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql

from dbutils.pooled_db import PooledDB


class MysqlPool:
    config = {
        'creator': pymysql,
        'host': "192.168.1.146",
        'port': 3306,
        'user': "root",
        'password': "345466",
        'db': "test",
        'charset': 'utf8',
        'maxconnections': 30,  # 连接池最大连接数量
        'cursorclass': pymysql.cursors.DictCursor
    }

    pool = PooledDB(**config)

    def __enter__(self):
        self.conn = MysqlPool.pool.connection()
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, type, value, trace):
        self.cursor.close()
        self.conn.close()

def db_conn(func):
    def wrapper(*args, **kw):
        with MysqlPool() as db:
            result = func(db, *args, **kw)
        return result
    return wrapper

# 实际应用的地方
class Mysql_Db_Manage:

    """table: register_phone"""
    @staticmethod
    @db_conn
    def update_data(db,sql):
        try:
            db.cursor.execute(sql)
            db.conn.commit()
        except:
            return -1
        return 1

    """table: register_phone"""
    @staticmethod
    @db_conn
    def is_have(db,sql):
        db.cursor.execute(sql)
        result = db.cursor.fetchone()
        print(result)
        if result is None:
            return False
        return True

    """table: register_phone"""
    @staticmethod
    @db_conn
    def select_one_data(db,sql):
        db.cursor.execute(sql)
        result = db.cursor.fetchone()
        return result


    """table: register_phone"""
    @staticmethod
    @db_conn
    def select_All_data(db,sql):
        db.cursor.execute(sql)
        result = db.cursor.fetchall()
        return result