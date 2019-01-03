# -*- coding:utf-8 -*-
# !/usr/bin/env python3
"""
Author     : Alexis
Email      : liub@midu.com
ProjectName: qqmusic
Flie       : sql.py
Time       : 2019-1-3 22:21
"""
import pymysql


class mysql():
    def __init__(self):
        self.conn = pymysql.connect(
                            user='root',
                            passwd='root',
                            db='qqmusic')
        self.cursor = self.conn.cursor()

    def inster(self, sql):
        self.cursor.execute(sql)

    def commit_data(self):
        self.conn.commit()

    def close_db(self):
        self.conn.close()


if __name__ == '__main__':
    x = mysql()