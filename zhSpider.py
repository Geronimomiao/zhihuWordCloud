# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     zhuihuSpider
   Description : 爬取知乎 高票回答信息 以用于生成词云
   Author :       wsm
   date：          2019-01-16
-------------------------------------------------
   Change Activity:
                   2019-01-16:
-------------------------------------------------
"""
__author__ = 'wsm'

# https://www.zhihu.com/api/v4/questions/267653585/answers?include=content,data[*].voteup_count&limit=20&offset=0

import json, os, requests
from pyquery import PyQuery

class ZhiHuSpider(object):
    def __init__(self, questionid):
        self.header = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'
        }
        self.questionid = questionid
        self.url = 'https://www.zhihu.com/api/v4/questions/' + self.questionid + '/answers?include=content,data[*].voteup_count&limit=20&offset=0'
        self.path = os.path.dirname(__file__)


    def getContent(self):
        json_str = requests.get(self.url, headers=self.header)
        json_obj = json.loads(json_str.content.decode('utf8'))

        content = json_obj['data']
        if content:
            self.url = json_obj['paging']['next']

            for i in content:
                # 过滤 html 标签
                doc = PyQuery(i['content'])
                self.formatContent(doc.text())
        else:
            self.url = ''


    def formatContent(self, content):
        with open(os.path.join(self.path, 'text/' + self.questionid + '.txt'), 'a+') as f:
            f.write(content + '\n')
            f.close()

    def run(self):
        while True:
            if self.url == '':
                break
            self.getContent()
        print('close')


if __name__ == '__main__':
    zsp = ZhiHuSpider('281036323')
    zsp.run()