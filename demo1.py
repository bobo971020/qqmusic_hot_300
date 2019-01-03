# -*- coding:utf-8 -*-
# !/usr/bin/env python3
"""
Author     : Alexis
Email      : liub@midu.com
ProjectName: qqmusic
Flie       : demo1.py
Time       : 2019-1-3 20:42


"""
import requests
import re
import os
from sql import mysql


class QQMUSIC(object):

    """
    获取QQ音乐热门音乐top300
    """
    def __init__(self):
        self.HEAD = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
            }

        self.FILE_NAME = "music.txt"
        self.HTML_DEMO = "html_demo.html"
        self.RANK = 1        # 统计排名
        self.SONG_BEGIN = 0
        self.PAGE = 1

    def check_dir(self, file):
        if os.path.exists(file):
            os.remove(file)

    def get_html(self, number):
            url = "https://c.y.qq.com/v8/fcg-bin/fcg_v8_toplist_cp.fcg?" \
                  "tpl=3&page=detail&date=2019_00&topid=26&" \
                  "type=top&song_begin="+str(number)+"&song_num=1&" \
                  "g_tk=5381&loginUin=0&hostUin=0&format=json&" \
                  "inCharset=utf8&outCharset=utf-8&notice=0&" \
                  "platform=yqq.json&needNewCode=0"
            prseon = requests.get(url, headers=self.HEAD)
            song = re.compile(r'"name\W{3}(.*?)"', re.S)
            song_data = re.search(song, prseon.text).group(1)       # 获取歌手名字
            Rank = re.compile('cur_count\W{3}(.*?)"', re.S)
            Rank_data = re.search(Rank, prseon.text).group(1)
            albumname = re.compile(r'albumname\W{3}(.*?)","', re.S)
            albumname_data = re.search(albumname, prseon.text).group(1)
            songname = re.compile(r'songname\W{3}(.*?)","', re.S)
            songname_data = re.search(songname, prseon.text).group(1)
            column = ('Rank', 'songname', 'song', 'albumname')
            data = (Rank_data, songname_data, song_data, albumname_data)
            sql = 'insert into music_data(' + (','.join(column)) + ')values("' + '","'.join(data) + '");'
            print(sql)
            return sql



if __name__ == '__main__':
    data_number = 300
    count = 0
    while count < data_number:
        s = mysql()
        m = QQMUSIC()
        s.inster(m.get_html(count))
        s.commit_data()
        s.close_db()
        count += 1


    # print(songname_data)  # 获取歌曲名称
    # print(song_data)  # 获取 专辑名称
    # print(Rank_data)  # 获取 排名
    # print(albumname_data)  # 获取歌手名字