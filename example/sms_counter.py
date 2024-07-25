#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os;
import sys;

from pprint import pprint;

sys.path.insert ( 0, os.path.dirname ( os.path.dirname ( os.path.abspath ( __file__ ) ) ) );
from sms.counter import SMSCounter;

from sms.counter import MAP_CHARS_7BIT, MAP_CHARS_7BIT_EX;

"""SMS counter"""
s = SMSCounter ();

"""All samples"""
DATASETS = [
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc hendrerit lacinia velit, in accumsan nibh euismod in. Nam pellentesque felis at efficitur vulputate. Pellentesque sit amet rutrum ante, sed iaculis nibh.', ## 7BIT
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eu mauris nisl. Nullam iaculis nec risus nec scelerisque -> €', ## 7BIT EX
    '', ## 7BIT Empty
    '遣ヨ村芝スゆざか重百ツサ中航ざのに見由常ミ約近れ銀田ラク場書ご多置そぱす願測フケウヘ川有覇車ルぞッ。' ## UTF16
];

for text in DATASETS:
    print ( ">> '{}'".format ( text ) );
    pprint ( s.count (
        sms_content = text
    ).dict () );
    print ( "\n" );

exit ( 0 );
