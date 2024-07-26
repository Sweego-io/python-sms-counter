# SMS Counter

**python-sms-counter** is a lib that help to count characters of SMS messages.

# How to use it

```python
from sms.counter import SMSCounter
>>> counter = SMSCounter ();
>>> counter.count ( 'ǂ some-string-to-be-counted' ).dict ();
>>> {'length': 29, 'messages': 1, 'remaining': 41, 'per_message': 70, 'encoding': 'UTF16'}
>>> {'chars_per_segment': 70,
     'chars_remaining': 43,
     'content': 'ǂ some-string-to-be-counted',
     'encoding': 'UTF16',
     'max_chars_available': 70,
     'segment': 1,
     'sms_size': 27}
```

The meaning of the `sms_size`, `chars_remaining` and `chars_per_segment` values returned by `count()` depend on the encoding. 

For `GSM_7BIT_EX` encoding, `sms_size`, `chars_remaining` and `chars_per_segment` count the number of 7-bit characters in the message, __including__ the escape character that must precede any characters in the "extended" character set. For example, the `sms_size` of the message '€' is 2, because it takes 2 7bit characters to encode '€' in `GSM_7BIT_EX`.

For `UTF16` and `GSM_7BIT` encoding, `sms_size`, `chars_remaining` and `chars_per_segment` count the number of characters (since all characters have an equal bit width).

All `GSM_7BIT` & `GSM_7BIT_EX` characters list : https://en.wikipedia.org/wiki/GSM_03.38

# Mentions

* Original idea : [dedayoa/sms-counter-python](https://github.com/dedayoa/sms-counter-python))

# License

MIT licensed. See the bundled [LICENSE](LICENSE) file for more details.

# Support

* Python : `>=3.9`
