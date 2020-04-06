#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dict
------------------

Test DictFire
------------------

:author:    hywell <opencoding@hotmail.com>
:homepage:  https://github.com/HeywoodKing
:license:   MIT, see LICENSE for more details.
:copyright: Copyright (c) 2020 hywell. All rights reserved
"""
from __future__ import unicode_literals
from dictfire import DictFire


def test_words_e2c(keyword):
    d = DictFire(['Test'])
    d.translate()
    out, err = keyword.readouterr()
    assert '测试' in out


def test_sentences_e2c(keyword):
    d = DictFire(['I', 'Love', 'You'])
    d.translate()
    out, err = keyword.readouterr()
    assert '我爱你' in out


def test_words_c2e(keyword):
    d = DictFire(['测试'])
    d.translate()
    out, err = keyword.readouterr()
    assert 'Test' in out


def test_sentences_c2e(keyword):
    d = DictFire(['我爱你'])
    d.translate()
    out, err = keyword.readouterr()
    assert 'I love you' in out
