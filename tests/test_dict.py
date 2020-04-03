#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dict
~~~~~~~~~

Test Dict

:author:    hywell <opencoding@hotmail.com>
:homepage:  https://github.com/HeywoodKing
:license:   MIT, see LICENSE for more details.
:copyright: Copyright (c) 2020 hywell. All rights reserved
"""
from __future__ import unicode_literals
from dictfire import DictFire


def test_words_e2c(keyword):
    DictFire(['Test'])
    out, err = keyword.readouterr()
    assert '测试' in out


def test_sentences_e2c(keyword):
    DictFire(['I', 'Love', 'You'])
    out, err = keyword.readouterr()
    assert '我爱你' in out


def test_words_c2e(keyword):
    DictFire(['测试'])
    out, err = keyword.readouterr()
    assert 'Test' in out


def test_sentences_c2e(keyword):
    DictFire(['我爱你'])
    out, err = keyword.readouterr()
    assert 'I love you' in out
