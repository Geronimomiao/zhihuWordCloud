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

# https://www.zhihu.com/api/v4/questions/267653585/answers?include=content,data[*].voteup_count&limit=20&offset=30

import json, os, requests
from pyquery import PyQuery

class zhihuSpider(object):
    def __init__(self):
        self.header = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'
        }
        self.url = 'https://www.zhihu.com/api/v4/questions/267653585/answers?include=content,data[*].voteup_count&limit=20&offset=30'
        self.path = os.path.dirname(__file__)


    def getContent(self):
        json_str = requests.get(self.url, headers=self.header)
        json_obj = json.loads(json_str.content.decode('utf8'))

        content = json_obj['data']
        for i in content:
            # 过滤 html 标签
            doc = PyQuery(i['content'])
            self.formatContent(doc.text())
        pass


        # data = json_obj.get('data')
        # if data:
        #     self.url = json_obj.get('paging').get('next')
        # else:
        #     self.url = ''
        #
        # for i in data:
        #     self.formatContent(i.get('content').encode("utf8"))

    def formatContent(self, content):
        with open(os.path.join(self.path, 'test.txt'), 'a+') as f:
            f.write(content + '\n')
            f.close()

    def run(self):
        self.getContent()


if __name__ == '__main__':
    zsp = zhihuSpider()
    zsp.run()