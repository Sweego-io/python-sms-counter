#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
import copy;

from pprint import pprint;
from unittest.mock import patch, Mock;


from sms.counter.sms_counter import ModelSMSCount, GSM_7BIT, GSM_7BIT_EX, UTF16;


DS = {
    'chars_per_segment': 123,
    'content': 'random-content',
    'encoding': GSM_7BIT,
    'sms_size': 456
};


class ModelSMSCount_constructorTest ( unittest.TestCase ):
    def test_required ( self ):
        ret = ModelSMSCount.parse_obj (
            DS
        );
        self.assertTrue ( True );
        
        self.assertEqual ( ret.chars_per_segment, 123 );
        self.assertEqual ( ret.chars_remaining, 36 );
        self.assertEqual ( ret.content, 'random-content' );
        self.assertEqual ( ret.encoding, GSM_7BIT );
        self.assertEqual ( ret.max_chars_available, 492 );
        self.assertEqual ( ret.segment, 4 );
        self.assertEqual ( ret.sms_size, 456 );

        
    def test_chars_per_segment_0 ( self ):
        ds = copy.deepcopy ( DS );
        ds [ 'sms_size' ] = 0;
        
        ret = ModelSMSCount.parse_obj (
            ds
        );
        self.assertTrue ( True );
        
        self.assertEqual ( ret.chars_per_segment, 123 );
        self.assertEqual ( ret.chars_remaining, 123 );
        self.assertEqual ( ret.content, 'random-content' );
        self.assertEqual ( ret.encoding, GSM_7BIT );
        self.assertEqual ( ret.max_chars_available, 123 );
        self.assertEqual ( ret.segment, 0 );
        self.assertEqual ( ret.sms_size, 0 );

    ## Test values
    
    def test_value_encoding_7bit ( self ):
        ds = copy.deepcopy ( DS );
        ds [ 'encoding' ] = GSM_7BIT;
        ret = ModelSMSCount.parse_obj (
            ds
        );
        self.assertEqual ( ret.encoding, GSM_7BIT );
        
    
    def test_value_encoding_7bit_ex ( self ):
        ds = copy.deepcopy ( DS );
        ds [ 'encoding' ] = GSM_7BIT_EX;
        ret = ModelSMSCount.parse_obj (
            ds
        );
        self.assertEqual ( ret.encoding, GSM_7BIT_EX );
        
    
    def test_value_encoding_utf16 ( self ):
        ds = copy.deepcopy ( DS );
        ds [ 'encoding' ] = UTF16;
        ret = ModelSMSCount.parse_obj (
            ds
        );
        self.assertEqual ( ret.encoding, UTF16 );


if __name__ == '__main__':
    unittest.main ();
