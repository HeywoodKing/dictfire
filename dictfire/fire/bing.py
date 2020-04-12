# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
dictfire

@File           : bing.py
@Time           : 2020/3/16 19:33
@Author         : hywell
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : dictfire
@description    : Chinese/English Translation
@homepage       : https://github.com/HeywoodKing/dictfire.git
@license        : MIT, see LICENSE for more details.
@copyright      : Copyright (c) 2020 hywell. All rights reserved
"""
from __future__ import absolute_import, unicode_literals
import re
# import asyncio
# import aiohttp
from urllib.parse import quote
import requests
from dictfire.setting import *


class Bing:
    """
    必应翻译服务
    """

    def __init__(self):
        self.src = None
        self.url = BING_URL
        self.header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7",
            # "Cache-Control": "max-age=0",
            # "Connection": "keep-alive",
            "Host": "fanyi.youdao.com",
            # "Upgrade-Insecure-Requests": "1",
            "User-Agent": UA.random,
        }
        # self.session = aiohttp.ClientSession(headers=self.header)

    def _parse(self, content):
        """
        解析内容
        """
        code = content['errorCode']
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
        except Exception as ex:
            code = -1
            src = self.src
            tgt = None
            msg = ex

        return {
            "code": code,
            "type": content['type'],
            "src": src,
            "tgt": tgt,
            "msg": msg
        }

    def _request(self, url=None, text=None):
        """
        请求远程api服务
        """
        try:
            if url is None:
                url = self.url

            if text is not None:
                url = url + quote(text.encode('utf-8'))
                # async with self.session.get(self.url) as resp:
                #     content = await resp.json(encoding='utf8')
                resp = requests.get(url)
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

    def translate(self, text):
        """
        根据输入内容翻译并返回翻译结果
        :param text:
        :return:
        """
        try:
            self.src = text
            resp = self._request(YOUDAO_URL, text)
            if resp['code'] == 0:
                result = self._parse(resp['content'])
            else:
                result = {
                    "code": resp['code'],
                    "type": None,
                    "src": text,
                    "tgt": text,
                    "msg": resp['content']
                }

            return result
        except Exception as ex:
            raise Exception('ERROR: remote service error! {}'.format(ex))


def main():
    Bing().translate("hello world")


if __name__ == '__main__':
    main()

