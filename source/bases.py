#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

import math


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Decode digits from binary (base 2)
    if base == 2:
        decoded_number = 0
        for bit in range(len(digits)):
            decoded_number += int(digits[-1 - bit]) * (2 ** bit)
        return decoded_number

    # Decode digits from hexadecimal (base 16)
    if base == 16:
        decoded_number = 0
        for digit in range(len(digits)):
            # Only accepts lowercase letters
            decoded_number += string.hexdigits.index(digits[-1 - digit]) * (16 ** digit)
        return decoded_number

    #  Decode digits from any base (2 up to 36)
    decoded_number = 0
    all_digits = string.digits + string.ascii_lowercase
    for digit in range(len(digits)):
        print(digits[-1 - digit], digit)
        # Only accepts lowercase letters
        decoded_number += all_digits.index(digits[-1 - digit]) * (base ** digit)
    return decoded_number


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    if base == 2:
        exponent = 0
        while number / 2 >= 1:
            number /= 2
            exponent += 1

        number = number * (2 ** exponent)
        encoded_number = ''
        while exponent >= 0:
            if number >= (2 ** exponent):
                encoded_number += '1'
                number -= (2 ** exponent)
            else:
                encoded_number += '0'

            print(exponent, encoded_number)
            exponent -= 1

        return encoded_number

    # TODO: Encode number in hexadecimal (base 16)
    if base == 16:
        exponent = 0
        while number / 16 >= 1:
            number /= 16
            exponent += 1

        number = round(number * (16 ** exponent))
        encoded_number = ''
        while exponent >= 0:
            if number >= (16 ** exponent):
                placeholder_value = math.floor(number / (16 ** exponent))
                encoded_number += string.printable[placeholder_value]
                number -= placeholder_value * (16 ** exponent)
            else:
                encoded_number += '0'

            exponent -= 1

        return encoded_number

    # TODO: Encode number in any base (2 up to 36)
    exponent = 0
    while number / base >= 1:
        number /= base
        exponent += 1

    number = round(number * (base ** exponent))
    encoded_number = ''
    while exponent >= 0:
        if number >= (base ** exponent):
            placeholder_value = math.floor(number / (base ** exponent))
            print(number, (base ** exponent))
            print(number / (base ** exponent))
            encoded_number += string.printable[placeholder_value]
            number -= placeholder_value * (base ** exponent)
        else:
            encoded_number += '0'

        exponent -= 1

    return encoded_number


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    # main()
    # print(decode('4ea2', 30))
    print(encode(2344, 10))
    print(encode(2345, 10))
    print(encode(2346, 10))
