#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
import copy;

from pprint import pprint;
from unittest.mock import patch, Mock;


from sms.counter.sms_counter import GSM_7BIT_EX, SEGMENT_LEN_GSM_7BIT_EX, SEGMENT_LEN_GSM_7BIT_EX_MULTIPART;
from sms.counter.sms_counter import CHARS_7BIT_EX, MAP_CHARS_7BIT_EX;


class const_7bit_exTest ( unittest.TestCase ):
    def test_encoding ( self ):
        self.assertEqual ( type ( GSM_7BIT_EX ), str );
        self.assertTrue ( len ( GSM_7BIT_EX ) > 0 );

        
    def test_len_segment ( self ):
        self.assertEqual ( type ( SEGMENT_LEN_GSM_7BIT_EX ), int );
        self.assertTrue ( SEGMENT_LEN_GSM_7BIT_EX > 0 );

        
    def test_len_segment_multipart ( self ):
        self.assertEqual ( type ( SEGMENT_LEN_GSM_7BIT_EX_MULTIPART ), int );
        self.assertTrue ( SEGMENT_LEN_GSM_7BIT_EX_MULTIPART > 0 );


    def test_chars ( self ):
        self.assertEqual ( type ( CHARS_7BIT_EX ), str );
        self.assertTrue ( len ( CHARS_7BIT_EX ) > 0 );


    def test_chars_map ( self ):
        self.assertEqual ( type ( MAP_CHARS_7BIT_EX ), list );
        self.assertEqual ( len ( MAP_CHARS_7BIT_EX ), len ( CHARS_7BIT_EX ) );
        
        

if __name__ == '__main__':
    unittest.main ();
