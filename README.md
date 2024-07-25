# SMS Counter

**python-sms-counter** is a lib that help to count characters of SMS messages.

# How to use it

```python
from sms.counter import SMSCounter
>>> counter = SMSCounter ();
>>> counter.count ( 'ǂ some-string-to-be-counted ' );
>>> {'length': 29, 'messages': 1, 'remaining': 41, 'per_message': 70, 'encoding': 'UTF16'}
```

The meaning of the `length`, `remaining` and `per_message` values returned by `count()` depend on the encoding. 

For GSM_7BIT_EX encoding, `length`, `remaining` and `per_message` count the number of 7-bit characters in the message, __including__ the escape character that must precede any characters in the "extended" character set. For example, the `length` of the message '€' is 2, because it takes 2 7bit characters to encode '€' in GSM_7BIT_EX.

For UTF16 and GSM_7BIT encoding, `length`, `remaining` and `per_message` count the number of characters (since all characters have an equal bit width).

# Mentions

* Original idea : [dedayoa/sms-counter-python](https://github.com/dedayoa/sms-counter-python))

# License

MIT licensed. See the bundled [LICENSE](LICENSE) file for more details.

# Support

* Python : `>=3.9`
