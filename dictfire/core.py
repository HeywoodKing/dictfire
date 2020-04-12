# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
dictfire

@File           : core.py
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
import math
import argparse
from dictfire.setting import *


class DictFire:
    """
    方便简洁强大的命令行翻译工具
    """

    def __init__(self, is_command=True):
        self.src = "hello world"
        self.trans_type = {
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

        parser = argparse.ArgumentParser(description='dictfire 是一款强大实用的互翻译工具')
        parser.add_argument(
            "-y", "--youdao",
            help="基于有道翻译提供服务",
            default=True,
            action="store_true"
        )
        parser.add_argument(
            "-b", "--baidu",
            help="基于百度翻译提供服务",
            # default=BAIDU_URL,
            action="store_true"
        )
        parser.add_argument(
            "-p", "--powerword",
            help="基于金山词霸翻译提供服务",
            action="store_true"
        )
        parser.add_argument(
            "-g", "--google",
            help="基于谷歌翻译提供服务",
            action="store_true"
        )
        parser.add_argument(
            "-m", "--bing",
            help="基于微软必应翻译提供服务",
            action="store_true"
        )

        if is_command:
            parser.add_argument("text", metavar="text", help="输入待翻译的文本,如果是单词可以不用加引号，如果是句子必须要加引号")
        self.args = parser.parse_args()

    def _print_error(self, error):
        """
        打印失败的结果
        """
        print(PRINT_SYMBOL * PRINT_SYMBOL_NUMS)
        print('{} {}'.format(PRINT_SYMBOL, error))
        print(PRINT_SYMBOL)
        print(PRINT_SYMBOL * PRINT_SYMBOL_NUMS)

    def _print_success(self, t, src, tgt):
        """
        打印成功的结果
        """
        print('\033[1;31m{} \033[0m'.format(PRINT_SYMBOL * PRINT_SYMBOL_NUMS))
        print('\033[1;31m# \033[0m')
        print('\033[1;31m# \033[0m {0}'.format(t))
        if re.match('[ \u4e00 -\u9fa5]+', src) is None:
            # 不包含中文
            src_columns = PRINT_SYMBOL_NUMS
        else:
            src_columns = len(src.encode('gbk'))

        if re.match('[ \u4e00 -\u9fa5]+', tgt):
            # 包含中文
            tgt_columns = len(tgt.encode('gbk'))
        else:
            tgt_columns = PRINT_SYMBOL_NUMS

        print('\033[1;31m# \033[0m')
        lines = math.ceil(src_columns / PRINT_SYMBOL_NUMS)
        for line in range(lines):
            start_index = line * PRINT_SYMBOL_NUMS
            end_index = start_index + PRINT_SYMBOL_NUMS
            print('\033[1;31m# \033[0m {0}'.format(src[start_index: end_index]))

        print('\033[1;31m# \033[0m')
        lines = math.ceil(tgt_columns / (PRINT_SYMBOL_NUMS - 2))
        for line in range(lines):
            start_index = line * (PRINT_SYMBOL_NUMS - 2)
            end_index = start_index + (PRINT_SYMBOL_NUMS - 2)
            print('\033[1;31m# \033[0m {0}'.format(tgt[start_index: end_index]))

        print('\033[1;31m# \033[0m')
        print('\033[1;31m{} \033[0m'.format(PRINT_SYMBOL * PRINT_SYMBOL_NUMS))

    def _translate(self, flag='youdao'):
        if flag == 'youdao':
            # 基于有道翻译服务
            from dictfire.fire.youdao import YouDao
            result = YouDao().translate(self.src)
        elif flag == 'baidu':
            # 基于百度翻译服务
            from dictfire.fire.baidu import BaiDu
            result = BaiDu().translate(self.src)
        elif flag == "google":
            # 基于谷歌翻译服务
            from dictfire.fire.google import Google
            result = Google().translate(self.src)
        elif flag == "bing":
            # 基于必应翻译服务
            from dictfire.fire.bing import Bing
            result = Bing().translate(self.src)
        elif flag == "powerword":
            # 基于金山词霸翻译服务
            from dictfire.fire.powerword import PowerWord
            result = PowerWord().translate(self.src)
        else:
            # 基于有道翻译服务
            from dictfire.fire.youdao import YouDao
            result = YouDao().translate(self.src)

        if result['code'] == 0:
            trans_type = self.trans_type.get(result['type'], None)
            self._print_success(trans_type, result['src'], result['tgt'])
        else:
            self._print_error(result['msg'])

    def translate(self, args=None):
        if args:
            # 表示程序调用，非命令行使用
            self.src = args
        else:
            try:
                # 表示命令行使用，非程序调用
                self.src = self.args.text
            except:
                pass

        try:
            if self.args.baidu:
                self._translate('baidu')
                return

            if self.args.google:
                self._translate('google')
                return

            if self.args.bing:
                self._translate('bing')
                return

            if self.args.powerword:
                self._translate('powerword')
                return

            if self.args.youdao:
                self._translate('youdao')
                return

        except Exception as ex:
            self._print_error(ex)


def main():
    # 命令行输入关键字 dict 空格后面的输入当做参数
    # d = DictFire(sys.argv[1:])
    # d.translate()

    # DictFire().translate(sys.argv[1:])

    # 命令行输入关键字 dict (输入可选项参数和必填文本)
    DictFire(is_command=False).translate()


if __name__ == '__main__':
    main()

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(DictFire(), )
