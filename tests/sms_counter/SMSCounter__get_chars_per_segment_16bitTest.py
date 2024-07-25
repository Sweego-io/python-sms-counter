#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
import random;

from pprint import pprint;
from unittest.mock import patch, Mock;


from sms.counter.sms_counter import SMSCounter, SEGMENT_LEN_GSM_7BIT_EX, SEGMENT_LEN_GSM_7BIT_EX_MULTIPART;
from sms.counter.sms_counter import MAP_CHARS_7BIT, MAP_CHARS_7BIT_EX;


DS_SMS_CODES = [];
for i in range ( 0, 12 ):
    DS_SMS_CODES.append ( random.choice ( MAP_CHARS_7BIT ) );
for i in range ( 0, 5 ):
    DS_SMS_CODES.append ( random.choice ( MAP_CHARS_7BIT_EX ) );
        
            
class SMSCounter__get_chars_per_segment_7bit_exTest ( unittest.TestCase ):
    def test_one_page ( self ):
        s = SMSCounter ();
        
        ret = s._get_chars_per_segment_7bit_ex (
            sms_codes = DS_SMS_CODES,
            sms_size = len ( DS_SMS_CODES )
        );
        
        self.assertEqual ( ret, (
            22,
            SEGMENT_LEN_GSM_7BIT_EX,
        ) );

        
    def test_multipart ( self ):
        s = SMSCounter ();
        
        ret = s._get_chars_per_segment_7bit_ex (
            sms_codes = DS_SMS_CODES,
            sms_size = len ( DS_SMS_CODES ) * 10
        );
        
        self.assertEqual ( ret, (
            ( len ( DS_SMS_CODES ) * 10 + 5 ),
            SEGMENT_LEN_GSM_7BIT_EX_MULTIPART,
        ) );

            
if __name__ == '__main__':
    unittest.main ();
