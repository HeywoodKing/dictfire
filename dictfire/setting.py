# -*- encoding: utf-8 -*-
"""
@File           : setting
@Time           : 2019/12/23
@Author         : hywell
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : dictfire
@description    : 描述
"""
import os
# import sys
from fake_useragent import UserAgent

# BASE_DIR = os.path.basename(os.path.basename(__file__))
# sys.argv.append(BASE_DIR)

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(BASE_DIR)

UA = UserAgent(
    verify_ssl=False,
    path=os.path.dirname(os.path.abspath(__file__)).replace('\\', '/') + '/fake_useragent_v0.1.11.json'
)

# 输出打印格式的#的数量
PRINT_SYMBOL_NUMS = 62
PRINT_SYMBOL = '#'

# 有道翻译地址
# YOUDAO_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
YOUDAO_URL = 'http://fanyi.youdao.com/translate?&doctype=json&type=AUTO&i='

# 金山词霸翻译地址
POWERWORD_URL = ''

# 百度翻译地址
BAIDU_URL = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
# BAIDU_URL = 'https://fanyi-api.baidu.com/api/trans/vip/translate'

# 谷歌翻译地址
GOOGLE_URL = ''

# 必应翻译地址
BING_URL = ''

# 译云翻译
YEEKIT = 'http://api.yeekit.com/dotranslate.php'
