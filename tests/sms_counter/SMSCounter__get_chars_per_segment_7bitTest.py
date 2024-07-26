#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;

from pprint import pprint;
from unittest.mock import patch, Mock;


from sms.counter.sms_counter import SMSCounter, SEGMENT_LEN_GSM_7BIT, SEGMENT_LEN_GSM_7BIT_MULTIPART;


class SMSCounter__get_chars_per_segment_7bitTest ( unittest.TestCase ):
    def test_one_page ( self ):
        s = SMSCounter ();
        
        ret = s._get_chars_per_segment_7bit (
            sms_size = SEGMENT_LEN_GSM_7BIT
        );
        
        self.assertEqual ( ret, SEGMENT_LEN_GSM_7BIT );

        
    def test_multipart ( self ):
        s = SMSCounter ();
        
        ret = s._get_chars_per_segment_7bit (
            sms_size = ( SEGMENT_LEN_GSM_7BIT + 1 )
        );
        
        self.assertEqual ( ret, SEGMENT_LEN_GSM_7BIT_MULTIPART );
                        
            
if __name__ == '__main__':
    unittest.main ();
