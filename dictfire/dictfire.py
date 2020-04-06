# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
dictfire

@File           : dictfire.py
@Time           : 2020/3/16 19:33
@Author         : hywell
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : dictfire
@description    : Chinese/English Translation
@homepage:  https://github.com/HeywoodKing/dictfire.git
@license:   MIT, see LICENSE for more details.
@copyright: Copyright (c) 2020 hywell. All rights reserved
"""

# from __future__ import unicode_literals
import sys
import re
# import json
# import aiohttp
import math
from urllib.parse import quote
from fake_useragent import UserAgent
# import asyncio
import requests

# __name__ = 'dict-fire'
__version__ = '1.0.0'
__description__ = """命令行下[中英，中俄，中日，中韩，中法，中德，中西]文互翻译工具（Command line translation tool for Chinese English,
Chinese French, Chinese Japanese, Chinese Korean, Chinese German）"""
__keywords__ = """Translation English2Chinese, Chinese2English, Chinese2French, French2Chinese, Chinese2Japanese,
Japanese2Chinese, Chinese2Korean, Korean2Chinese, Chinese2German, German2Chinese） Command-line"""
__author__ = 'hywell'
__contact__ = 'opencoding@hotmail.com'
__url__ = 'git@github.com:HeywoodKing/dictfire.git'
__license__ = 'MIT'


class DictFire:
    """
    方便简洁强大的命令行翻译工具
    """

    def __init__(self, argv=None):
        self.src = argv if argv else ['hello world']
        self.ua = UserAgent(verify_ssl=False)
        self.url = 'http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i='
        self.header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7",
            # "Cache-Control": "max-age=0",
            # "Connection": "keep-alive",
            "Host": "fanyi.youdao.com",
            # "Upgrade-Insecure-Requests": "1",
            "User-Agent": self.ua.random,
        }
        self.auto_type = {
            "ZH_CN2EN": "中文　»　英语",
            "ZH_CN2JA": "中文　»　日语",
            "ZH_CN2KR": "中文　»　韩语",
            "ZH_CN2FR": "中文　»　法语",
            "ZH_CN2RU": "中文　»　俄语",
            "ZH_CN2SP": "中文　»　西语",
            "EN2ZH_CN": "英语　»　中文",
            "JA2ZH_CN": "日语　»　中文",
            "KR2ZH_CN": "韩语　»　中文",
            "FR2ZH_CN": "法语　»　中文",
            "RU2ZH_CN": "俄语　»　中文",
            "SP2ZH_CN": "西语　»　中文",
        }
        self.number_flag = 68
        # self.session = aiohttp.ClientSession(headers=self.header)

    def _print_error(self, error):
        """
        打印失败的结果
        """
        print('*' * self.number_flag)
        print('* {}'.format(error))
        print('*')
        print('*' * self.number_flag)

    def _print_success(self, t, src, tgt):
        """
        打印成功的结果
        """
        print('\033[1;31m{} \033[0m'.format('#' * self.number_flag))
        print('\033[1;31m# \033[0m')
        print('\033[1;31m# \033[0m {0}'.format(t))
        if re.match('[ \u4e00 -\u9fa5]+', src) is None:
            # 不包含中文
            src_columns = self.number_flag
        else:
            src_columns = len(src.encode('gbk'))

        if re.match('[ \u4e00 -\u9fa5]+', tgt):
            # 包含中文
            tgt_columns = len(tgt.encode('gbk'))
        else:
            tgt_columns = self.number_flag

        print('\033[1;31m# \033[0m')
        lines = math.ceil(src_columns / self.number_flag)
        for line in range(lines):
            start_index = line * self.number_flag
            end_index = start_index + self.number_flag
            print('\033[1;31m# \033[0m {0}'.format(src[start_index: end_index]))

        # print('\033[1;31m# \033[0m')
        lines = math.ceil(tgt_columns / (self.number_flag - 2))
        for line in range(lines):
            start_index = line * (self.number_flag - 2)
            end_index = start_index + (self.number_flag - 2)
            print('\033[1;31m# \033[0m {0}'.format(tgt[start_index: end_index]))

        print('\033[1;31m# \033[0m')
        print('\033[1;31m{} \033[0m'.format('#' * self.number_flag))

    def _parse(self, content):
        """
        解析内容
        """
        code = content['errorCode']
        t = self.auto_type.get(content['type'], None)  # type
        try:
            src = content['translateResult'][0][0]['src']  # source
            if code == 0:  # Success
                tgt = content['translateResult'][0][0]['tgt']  # result
                msg = '获取成功'
            elif code == 20:
                # print('WORD TO LONG')
                tgt = None
                msg = 'WORD TO LONG'
            elif code == 30:
                # print('TRANSLATE ERROR')
                tgt = None
                msg = 'TRANSLATE ERROR'
            elif code == 40:
                # print('DON\'T SUPPORT THIS LANGUAGE')
                tgt = None
                msg = 'DON\'T SUPPORT THIS LANGUAGE'
            elif code == 50:
                # print('KEY FAILED')
                tgt = None
                msg = 'KEY FAILED'
            elif code == 60:
                # print('DON\'T HAVE THIS WORD')
                tgt = None
                msg = 'DON\'T HAVE THIS WORD'
            else:
                # print('UNKOWN')
                tgt = None
                msg = 'UNKOWN'
        except KeyError as ex:
            src = self.src
            tgt = None
            msg = ex

        return {
            "code": code,
            "type": t,
            "src": src,
            "tgt": tgt,
            "msg": msg
        }

    def _request(self):
        """
        请求远程api服务
        """
        try:
            message = ''
            if len(self.src) > 0:
                for s in self.src:
                    message = message + s + ' '

                self.url = self.url + quote(message.encode('utf-8'))
                # async with self.session.get(self.url) as resp:
                #     content = await resp.json(encoding='utf8')
                resp = requests.get(self.url)
                content = resp.json(encoding='utf8')
                code = 0
            else:
                code = 1
                content = 'Usage: dict fire'
        except Exception as ex:
            code = -1
            content = 'ERROR: Network or remote service error! {}'.format(ex)

        return {
            "code": code,
            "content": content
        }

    def _translate(self):
        try:
            resp = self._request()
            if resp['code'] == 0:
                result = self._parse(resp['content'])
                if result['code'] == 0:
                    self._print_success(result['type'], result['src'], result['tgt'])
                else:
                    self._print_error(result['msg'])
            else:
                self._print_error(resp['content'])
        except Exception as ex:
            self._print_error('ERROR: remote service error! {}'.format(ex))

    def translate(self, argv=None):
        if argv:
            self.src = argv

        self._translate()


if __name__ == '__main__':
    # dict = DictFire(sys.argv[1:])
    # dict.translate()

    dict = DictFire()
    dict.translate(sys.argv[1:])

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(DictFire(), )
