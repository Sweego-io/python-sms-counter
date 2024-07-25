#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;

from pprint import pprint;
from unittest.mock import patch, Mock;


from sms.counter.sms_counter import SMSCounter;


class SMSCounter__convert_text_to_codesTest ( unittest.TestCase ):
    def test_convert ( self ):
        s = SMSCounter ();

        ret = s._convert_text_to_codes (
            sms_content = 'random-string'
        );

        self.assertEqual ( type ( ret ), list );
        self.assertEqual ( len ( ret ), len ( 'random-string' ) );
        for i in ret:
            self.assertEqual ( type ( i ), int, i );
                        
            
if __name__ == '__main__':
    unittest.main ();
