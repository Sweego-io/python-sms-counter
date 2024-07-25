#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
import random;

from pprint import pprint;
from unittest.mock import patch, Mock;


from sms.counter.sms_counter import SMSCounter, GSM_7BIT, GSM_7BIT_EX, UTF16;
from sms.counter.sms_counter import MAP_CHARS_7BIT, MAP_CHARS_7BIT_EX;

            
class SMSCounter_get_encodingTest ( unittest.TestCase ):
    def test_7_bit ( self ):
        with patch ( 'sms.counter.sms_counter.SMSCounter._convert_text_to_codes' ) as convert_text_to_codes:
            ds_sms_codes = [];
            for i in range ( 0, 12 ):
                ds_sms_codes.append ( random.choice ( MAP_CHARS_7BIT ) );
            convert_text_to_codes.return_value = ds_sms_codes;
            
            s = SMSCounter ();
        
            ret = s.get_encoding (
                sms_content = 'random-sms-content'
            );
        
            self.assertEqual ( ret, GSM_7BIT );

            convert_text_to_codes.assert_called_once_with (
                sms_content = 'random-sms-content'
            );

            
    def test_7_bit_ex ( self ):
        with patch ( 'sms.counter.sms_counter.SMSCounter._convert_text_to_codes' ) as convert_text_to_codes:
            ds_sms_codes = [];
            for i in range ( 0, 12 ):
                ds_sms_codes.append ( random.choice ( MAP_CHARS_7BIT ) );
            for i in range ( 0, 12 ):
                ds_sms_codes.append ( random.choice ( MAP_CHARS_7BIT_EX ) );
            convert_text_to_codes.return_value = ds_sms_codes;
            
            s = SMSCounter ();
            
            ret = s.get_encoding (
                sms_content = 'random-sms-content'
            );
            
            self.assertEqual ( ret, GSM_7BIT_EX );

            convert_text_to_codes.assert_called_once_with (
                sms_content = 'random-sms-content'
            );

            
    def test_16_bit ( self ):
        with patch ( 'sms.counter.sms_counter.SMSCounter._convert_text_to_codes' ) as convert_text_to_codes:
            ds_sms_codes = [];
            for i in range ( 0, 12 ):
                ds_sms_codes.append ( random.choice ( MAP_CHARS_7BIT ) );
            for i in range ( 0, 12 ):
                ds_sms_codes.append ( random.choice ( MAP_CHARS_7BIT_EX ) );
            ds_sms_codes.append ( 0 );
            convert_text_to_codes.return_value = ds_sms_codes;
            
            s = SMSCounter ();
            
            ret = s.get_encoding (
                sms_content = 'random-sms-content'
            );
            
            self.assertEqual ( ret, UTF16 );

            convert_text_to_codes.assert_called_once_with (
                sms_content = 'random-sms-content'
            );
        
            
if __name__ == '__main__':
    unittest.main ();
