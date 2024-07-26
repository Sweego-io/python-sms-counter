#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;

from pprint import pprint;
from unittest.mock import patch, Mock;


from sms.counter.sms_counter import SMSCounter, SEGMENT_LEN_UTF16, SEGMENT_LEN_UTF16_MULTIPART;


class SMSCounter__get_chars_per_segment_utf16Test ( unittest.TestCase ):
    def test_one_page ( self ):
        s = SMSCounter ();
        
        ret = s._get_chars_per_segment_utf16 (
            sms_size = SEGMENT_LEN_UTF16
        );
        
        self.assertEqual ( ret, SEGMENT_LEN_UTF16 );

        
    def test_multipart ( self ):
        s = SMSCounter ();
        
        ret = s._get_chars_per_segment_utf16 (
            sms_size = ( SEGMENT_LEN_UTF16 + 1 )
        );
        
        self.assertEqual ( ret, SEGMENT_LEN_UTF16_MULTIPART );
                        
            
if __name__ == '__main__':
    unittest.main ();
