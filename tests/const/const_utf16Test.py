#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
import copy;

from pprint import pprint;
from unittest.mock import patch, Mock;


from sms.counter.sms_counter import UTF16, SEGMENT_LEN_UTF16, SEGMENT_LEN_UTF16_MULTIPART;


class const_utf16Test ( unittest.TestCase ):
    def test_encoding ( self ):
        self.assertEqual ( type ( UTF16 ), str );
        self.assertTrue ( len ( UTF16 ) > 0 );

        
    def test_len_segment ( self ):
        self.assertEqual ( type ( SEGMENT_LEN_UTF16 ), int );
        self.assertTrue ( SEGMENT_LEN_UTF16 > 0 );

        
    def test_len_segment_multipart ( self ):
        self.assertEqual ( type ( SEGMENT_LEN_UTF16_MULTIPART ), int );
        self.assertTrue ( SEGMENT_LEN_UTF16_MULTIPART > 0 );
        

if __name__ == '__main__':
    unittest.main ();
