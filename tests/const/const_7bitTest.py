#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
import copy;

from pprint import pprint;
from unittest.mock import patch, Mock;


from sms.counter.sms_counter import GSM_7BIT, SEGMENT_LEN_GSM_7BIT, SEGMENT_LEN_GSM_7BIT_MULTIPART;
from sms.counter.sms_counter import CHARS_7BIT, MAP_CHARS_7BIT;


class const_7bitTest ( unittest.TestCase ):
    def test_encoding ( self ):
        self.assertEqual ( type ( GSM_7BIT ), str );
        self.assertTrue ( len ( GSM_7BIT ) > 0 );

        
    def test_len_segment ( self ):
        self.assertEqual ( type ( SEGMENT_LEN_GSM_7BIT ), int );
        self.assertTrue ( SEGMENT_LEN_GSM_7BIT > 0 );

        
    def test_len_segment_multipart ( self ):
        self.assertEqual ( type ( SEGMENT_LEN_GSM_7BIT_MULTIPART ), int );
        self.assertTrue ( SEGMENT_LEN_GSM_7BIT_MULTIPART > 0 );


    def test_chars ( self ):
        self.assertEqual ( type ( CHARS_7BIT ), str );
        self.assertTrue ( len ( CHARS_7BIT ) > 0 );


    def test_chars_map ( self ):
        self.assertEqual ( type ( MAP_CHARS_7BIT ), list );
        self.assertEqual ( len ( MAP_CHARS_7BIT ), len ( CHARS_7BIT ) );
        
        

if __name__ == '__main__':
    unittest.main ();
