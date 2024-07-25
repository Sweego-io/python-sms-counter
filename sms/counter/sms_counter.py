#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import ceil;
from pprint import pprint;
from pydantic import BaseModel, root_validator, validate_arguments, Field;
from typing import Literal, Optional, List, Tuple;

#: Encoding name : 7BIT
GSM_7BIT = 'GSM_7BIT';
#: 7BIT segment length (1 page)
SEGMENT_LEN_GSM_7BIT = 160;
#: 7BIT segment length (more than 1 page)
SEGMENT_LEN_GSM_7BIT_MULTIPART = 153;

#: Encoding name : 7BIT EX
GSM_7BIT_EX = 'GSM_7BIT_EX';
#: 7BIT EX segment length (1 page)
SEGMENT_LEN_GSM_7BIT_EX = 160;
#: 7BIT EX segment length (more than 1 page)
SEGMENT_LEN_GSM_7BIT_EX_MULTIPART = 153;

#: Encoding name : 16BIT
UTF16 = 'UTF16';
#: 16BIT segment length (1 page)
SEGMENT_LEN_UTF16 = 70;
#: 16BIT segment length (more than 1 page)
SEGMENT_LEN_UTF16_MULTIPART = 67;

#: 7BIT all chars available as unicode code
MAP_CHARS_7BIT = [
    10, 12, 13, 32, # LF   FF   CR   Space
    33, 34, 35, 36, # !   "   #   $
    37, 38, 39, 40, # %   &   '   (
    41, 42, 43, 44, # )   *   +   ,
    45, 46, 47, 48, # -   .   /   0
    49, 50, 51, 52, # 1   2   3   4
    53, 54, 55, 56, # 5   6   7   8
    57, 58, 59, 60, # 9   :   ;   <
    61, 62, 63, 64, # =   >   ?   @
    65, 66, 67, 68, # A   B   C   D
    69, 70, 71, 72, # E   F   G   H
    73, 74, 75, 76, # I   J   K   L
    77, 78, 79, 80, # M   N   O   P
    81, 82, 83, 84, # Q   R   S   T
    85, 86, 87, 88, # U   V   W   X
    89, 90, 92, 95, # Y   Z   \   _
    97, 98, 99, 100, # a   b   c   d
    101, 102, 103, 104, # e   f   g   h
    105, 106, 107, 108, # i   j   k   l
    109, 110, 111, 112, # m   n   o   p
    113, 114, 115, 116, # q   r   s   t
    117, 118, 119, 120, # u   v   w   x
    121, 122, 161, 163, # y   z   ¡   £
    164, 165, 191, 196, # ¤   ¥   ¿   Ä
    197, 198, 199, 201, # Å   Æ   Ç   É
    209, 214, 216, 220, # Ñ   Ö   Ø   Ü
    223, 224, 228, 229, # ß   à   ä   å
    230, 232, 233, 236, # æ   è   é   ì
    241, 242, 246, 248, # ñ   ò   ö   ø
    249, 252, 915, 916, # ù   ü   Γ   Δ
    920, 923, 926, 928, # Θ   Λ   Ξ   Π
    931, 934, 936, 937 # Σ   Φ   Ψ   Ω
];

#: 7BIT EX all additional chars available as unicode code
MAP_CHARS_7BIT_EX = [
    91, 92, 93, # [   \   ]
    94, 123, 124, # ^   {   |
    125, 126, 8364 # }   ~   €
];


class ModelSMSCount ( BaseModel ):
    chars_per_segment: int = Field (
        description = 'Number of characters per segment'
    )
    chars_remaining: int = Field (
        description = 'Number of characters remaining before adding a new segment'
    )
    encoding: Literal [
        GSM_7BIT,
        GSM_7BIT_EX,
        UTF16
    ] = Field (
        description = 'Current text encoding'
    )
    max_chars_available: int = Field (
        description = 'Number of characters max for current number of segments'
    )
    segment: int = Field (
        description = 'Number of sms pages'
    )
    sms_size: int = Field (
        description = 'SMS number of characters'
    )
    
    
    @root_validator ( pre = True )
    def fill_fields ( cls, values: dict ) -> dict:
        """Fiell fields : segment / max_chars_available / chars_remaining
        
        Arguments:
            cls (ModelSMSCount): Class
            values (dict): Input values
        
        Returns:
            dict: Input values with new fields
        """
        values [ 'segment' ] = int (
            ceil ( values [ 'sms_size' ] / float ( values [ 'chars_per_segment' ] ) )
        );
        values [ 'max_chars_available' ] = ( values [ 'segment' ] * values [ 'chars_per_segment'] );
        values [ 'chars_remaining' ] = ( values [ 'max_chars_available' ] - values [ 'sms_size' ] );
        
        if ( values [ 'chars_per_segment' ] == 0 ):
            values [ 'chars_remaining' ] = values [ 'chars_per_segment' ];
            values [ 'max_chars_available' ] = values [ 'chars_per_segment' ];
        
        return values;


class SMSCounter:
    """Count sms content
    """
    def _convert_text_to_ord ( self, sms_content: str ) -> List [ int ]:
        """Convert sms content to list of char unicode code
        
        Arguments:
            sms_content (str): SMS content
        
        Returns:
            int[]: SMS content as list of unicode code
        """
        return [
            ord ( x ) for x in sms_content
        ];
    
    
    def _get_chars_per_segment_7bit ( self, sms_size: int ) -> int:
        """Get numbers of chars per segment for encoding : 7bit
        
        Arguments:
            sms_size (int): SMS size
        
        Returns:
            int: Number of chars per segment
        """
        if ( sms_size > SEGMENT_LEN_GSM_7BIT ):
            return SEGMENT_LEN_GSM_7BIT_MULTIPART;
        return SEGMENT_LEN_GSM_7BIT;
    
    
    def _get_chars_per_segment_7bit_ex ( self, sms_codes: List [ int ], sms_size: int ) -> Tuple [ int, int ]:
        """Get numbers of chars per segment for encoding : 7bit ex
        
        Arguments:
            sms_codes (int[]): SMS content as unicode codes
            sms_size (int): SMS size
        
        Returns:
            tuple(int,int): SMS size updated / Number of chars per segment
        """
        """All ex chars from the sms"""
        ex_chars = [ c for c in sms_codes if c in MAP_CHARS_7BIT_EX ];
        ## Double size of each ex chars
        sms_size += len ( ex_chars );
        
        if ( sms_size > SEGMENT_LEN_GSM_7BIT_EX ):
            return (
                sms_size,
                SEGMENT_LEN_GSM_7BIT_EX_MULTIPART,
            );
        
        return (
            sms_size,
            SEGMENT_LEN_GSM_7BIT_EX,
        );
    
    
    def _get_chars_per_segment_16bit ( self, sms_size: int ) -> int:
        """Get numbers of chars per segment for encoding : 16bit
        
        Arguments:
            sms_size (int): SMS size
        
        Returns:
            int: Number of chars per segment
        """
        if ( sms_size > SEGMENT_LEN_UTF16 ):
            return SEGMENT_LEN_UTF16_MULTIPART;
        return SEGMENT_LEN_UTF16; 
    
    
    @validate_arguments
    def get_encoding ( self, sms_content: str ) -> Literal [ GSM_7BIT, GSM_7BIT_EX, UTF16 ]:
        """Get sms encoding
        
        Arguments:
            sms_content (str): SMS text
        
        Returns:
            str: SMS text encoding value
        """
        """SMS content as unicode codes"""
        sms_codes = self._convert_text_to_ord (
            sms_content = sms_content
        );
        
        """SMS codes who are not allowed in 7bit"""
        non_gsm_7bit_chars = set ( sms_codes ) - set ( MAP_CHARS_7BIT );
        if ( len ( non_gsm_7bit_chars ) == 0 ):
            return GSM_7BIT;
        
        """SMS codes who are not allowed in 7bit EX"""
        non_gsm_7bit_ex_chars = non_gsm_7bit_chars - set ( MAP_CHARS_7BIT_EX );
        if ( len ( non_gsm_7bit_ex_chars ) == 0 ):
            return GSM_7BIT_EX;
        
        return UTF16;
    
    
    @validate_arguments
    def count ( self, sms_content: str ) -> ModelSMSCount:
        """Count sms
        
        Arguments:
            sms_content (str): SMS text
        
        Raises:
            Exception: if encoding not supported
        
        Returns:
            ModelSMSCount: SMS count data
        """
        """SMS content as unicode codes"""
        sms_codes = self._convert_text_to_ord (
            sms_content = sms_content
        );
        
        """SMS content encoding"""
        encoding = self.get_encoding (
            sms_content = sms_content
        );
        
        """SMS number of characters"""
        sms_size = len ( sms_codes );
        
        """Number of characters per segments"""
        chars_per_segment = None;
        
        if ( encoding == GSM_7BIT ):
            chars_per_segment = self._get_chars_per_segment_7bit (
                sms_size = sms_size
            );
            
        elif ( encoding == GSM_7BIT_EX ):
            ## Will sms size with number of ex chars
            (sms_size, chars_per_segment, ) = self._get_chars_per_segment_7bit_ex (
                sms_codes = sms_codes,
                sms_size = sms_size
            );
        
        elif ( encoding == UTF16 ):
            chars_per_segment = self._get_chars_per_segment_16bit (
                sms_size = sms_size
            );
            
        else:
            raise Exception ( 'Encoding not supported' );
        
        return ModelSMSCount (
            chars_per_segment = chars_per_segment,
            encoding = encoding,
            sms_size = sms_size
        );
