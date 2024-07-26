#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os;
import unittest;
import random;

from pprint import pprint;
from unittest.mock import patch, Mock;


from sms.counter.sms_counter import SMSCounter, GSM_7BIT, GSM_7BIT_EX, UTF16;


class SMSCounter_countTest ( unittest.TestCase ):
    def test_count_7bit ( self ):
        with patch ( 'sms.counter.sms_counter.SMSCounter._convert_text_to_codes' ) as convert_text_to_codes:
            with patch ( 'sms.counter.sms_counter.SMSCounter.get_encoding' ) as get_encoding:
                with patch ( 'sms.counter.sms_counter.SMSCounter._get_chars_per_segment_7bit' ) as get_per_segment_chars_7bit:
                    with patch ( 'sms.counter.sms_counter.SMSCounter._get_chars_per_segment_7bit_ex' ) as get_per_segment_chars_7bit_ex:
                        with patch ( 'sms.counter.sms_counter.SMSCounter._get_chars_per_segment_utf16' ) as get_per_segment_chars_utf16:
                            with patch ( 'sms.counter.sms_counter.ModelSMSCount' ) as m_init:
                                convert_text_to_codes.return_value = 'random-sms-codes';
                                get_encoding.return_value = GSM_7BIT;
                                get_per_segment_chars_7bit.return_value = 'random-chars-per-segment';
                                m_init.side_effect = Mock;
            
                                s = SMSCounter ();
                                
                                ret = s.count (
                                    sms_content = 'random-sms-content'
                                );
                                
                                self.assertTrue ( isinstance ( ret, Mock ) );
                                self.assertEqual ( ret.chars_per_segment, 'random-chars-per-segment' );
                                self.assertEqual ( ret.encoding, GSM_7BIT );
                                self.assertEqual ( ret.sms_size, len ( 'random-sms-codes' ) );

                                convert_text_to_codes.assert_called_once_with (
                                    sms_content = 'random-sms-content'
                                );
                                get_encoding.assert_called_once_with (
                                    sms_content = 'random-sms-content'
                                );
                                get_per_segment_chars_7bit.assert_called_once_with (
                                    sms_size = len ( 'random-sms-codes' )
                                );
                                get_per_segment_chars_7bit_ex.assert_not_called ();
                                get_per_segment_chars_utf16.assert_not_called ();
                                m_init.assert_called_once_with (
                                    chars_per_segment = 'random-chars-per-segment',
                                    encoding = GSM_7BIT,
                                    sms_size = len ( 'random-sms-codes' )
                                );

                                
    def test_count_7bit_ex ( self ):
        with patch ( 'sms.counter.sms_counter.SMSCounter._convert_text_to_codes' ) as convert_text_to_codes:
            with patch ( 'sms.counter.sms_counter.SMSCounter.get_encoding' ) as get_encoding:
                with patch ( 'sms.counter.sms_counter.SMSCounter._get_chars_per_segment_7bit' ) as get_per_segment_chars_7bit:
                    with patch ( 'sms.counter.sms_counter.SMSCounter._get_chars_per_segment_7bit_ex' ) as get_per_segment_chars_7bit_ex:
                        with patch ( 'sms.counter.sms_counter.SMSCounter._get_chars_per_segment_utf16' ) as get_per_segment_chars_utf16:
                            with patch ( 'sms.counter.sms_counter.ModelSMSCount' ) as m_init:
                                convert_text_to_codes.return_value = 'random-sms-codes';
                                get_encoding.return_value = GSM_7BIT_EX;
                                get_per_segment_chars_7bit_ex.return_value = (
                                    123,
                                    'random-chars-per-segment',
                                );
                                m_init.side_effect = Mock;
            
                                s = SMSCounter ();
                                
                                ret = s.count (
                                    sms_content = 'random-sms-content'
                                );
                                
                                self.assertTrue ( isinstance ( ret, Mock ) );
                                self.assertEqual ( ret.chars_per_segment, 'random-chars-per-segment' );
                                self.assertEqual ( ret.encoding, GSM_7BIT_EX );
                                self.assertEqual ( ret.sms_size, 123 );

                                convert_text_to_codes.assert_called_once_with (
                                    sms_content = 'random-sms-content'
                                );
                                get_encoding.assert_called_once_with (
                                    sms_content = 'random-sms-content'
                                );
                                get_per_segment_chars_7bit.assert_not_called ();
                                get_per_segment_chars_7bit_ex.assert_called_once_with (
                                    sms_codes = 'random-sms-codes',
                                    sms_size = len ( 'random-sms-codes' )
                                );
                                get_per_segment_chars_utf16.assert_not_called ();
                                m_init.assert_called_once_with (
                                    chars_per_segment = 'random-chars-per-segment',
                                    encoding = GSM_7BIT_EX,
                                    sms_size = 123
                                );

                                
    def test_count_utf_16 ( self ):
        with patch ( 'sms.counter.sms_counter.SMSCounter._convert_text_to_codes' ) as convert_text_to_codes:
            with patch ( 'sms.counter.sms_counter.SMSCounter.get_encoding' ) as get_encoding:
                with patch ( 'sms.counter.sms_counter.SMSCounter._get_chars_per_segment_7bit' ) as get_per_segment_chars_7bit:
                    with patch ( 'sms.counter.sms_counter.SMSCounter._get_chars_per_segment_7bit_ex' ) as get_per_segment_chars_7bit_ex:
                        with patch ( 'sms.counter.sms_counter.SMSCounter._get_chars_per_segment_utf16' ) as get_per_segment_chars_utf16:
                            with patch ( 'sms.counter.sms_counter.ModelSMSCount' ) as m_init:
                                convert_text_to_codes.return_value = 'random-sms-codes';
                                get_encoding.return_value = UTF16;
                                get_per_segment_chars_utf16.return_value = 'random-chars-per-segment';
                                m_init.side_effect = Mock;
                                
                                s = SMSCounter ();
                                
                                ret = s.count (
                                    sms_content = 'random-sms-content'
                                );
                                
                                self.assertTrue ( isinstance ( ret, Mock ) );
                                self.assertEqual ( ret.chars_per_segment, 'random-chars-per-segment' );
                                self.assertEqual ( ret.encoding, UTF16 );
                                self.assertEqual ( ret.sms_size, len ( 'random-sms-codes' ) );
                                
                                convert_text_to_codes.assert_called_once_with (
                                    sms_content = 'random-sms-content'
                                );
                                get_encoding.assert_called_once_with (
                                    sms_content = 'random-sms-content'
                                );
                                get_per_segment_chars_7bit.assert_not_called ();
                                get_per_segment_chars_7bit_ex.assert_not_called ();
                                get_per_segment_chars_utf16.assert_called_once_with (
                                    sms_size = len ( 'random-sms-codes' )
                                );
                                m_init.assert_called_once_with (
                                    chars_per_segment = 'random-chars-per-segment',
                                    encoding = UTF16,
                                    sms_size = len ( 'random-sms-codes' )
                                );

                                
    def test_unsupported_encoding ( self ):
        with patch ( 'sms.counter.sms_counter.SMSCounter._convert_text_to_codes' ) as convert_text_to_codes:
            with patch ( 'sms.counter.sms_counter.SMSCounter.get_encoding' ) as get_encoding:
                with patch ( 'sms.counter.sms_counter.SMSCounter._get_chars_per_segment_7bit' ) as get_per_segment_chars_7bit:
                    with patch ( 'sms.counter.sms_counter.SMSCounter._get_chars_per_segment_7bit_ex' ) as get_per_segment_chars_7bit_ex:
                        with patch ( 'sms.counter.sms_counter.SMSCounter._get_chars_per_segment_utf16' ) as get_per_segment_chars_utf16:
                            with patch ( 'sms.counter.sms_counter.ModelSMSCount' ) as m_init:
                                convert_text_to_codes.return_value = 'random-sms-codes';
                                get_encoding.return_value = 'another-encoding';
                                
                                s = SMSCounter ();

                                with self.assertRaises ( Exception ) as cm:
                                    s.count (
                                        sms_content = 'random-sms-content'
                                    );
                                
                                self.assertEqual ( str ( cm.exception ), 'Encoding not supported' );
                                
                                convert_text_to_codes.assert_called_once_with (
                                    sms_content = 'random-sms-content'
                                );
                                get_encoding.assert_called_once_with (
                                    sms_content = 'random-sms-content'
                                );
                                get_per_segment_chars_7bit.assert_not_called ();
                                get_per_segment_chars_7bit_ex.assert_not_called ();
                                get_per_segment_chars_utf16.assert_not_called ();
                                m_init.assert_not_called ();
        
            
if __name__ == '__main__':
    unittest.main ();
