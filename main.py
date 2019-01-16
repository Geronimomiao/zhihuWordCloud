# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main
   Description :    项目启动文件
   Author :       wsm
   date：          2019-01-16
-------------------------------------------------
   Change Activity:
                   2019-01-16:
-------------------------------------------------
"""
__author__ = 'wsm'


from zhWordCloud import ZhiHuWordCloud
from zhSpider import ZhiHuSpider


def begin(questionid, picname):
    ZhiHuSpider(questionid).run()
    ZhiHuWordCloud(questionid, picname).run()



if __name__ == '__main__':
    questionid = '281036323'
    picname = 't11.png'
    begin(questionid, picname)





