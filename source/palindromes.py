#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # Implement the is_palindrome function iteratively here
    lowercase_text = text.lower()
    left_index = 0
    right_index = len(text) - 1

    # Do while character indexes have not reached center of text
    while right_index > left_index:
        while lowercase_text[left_index] not in string.ascii_lowercase:
            left_index += 1
        while lowercase_text[right_index] not in string.ascii_lowercase:
            right_index -= 1

        if lowercase_text[left_index] != lowercase_text[right_index]:
            return False

        left_index += 1
        right_index -= 1

    return True
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    # Implement the is_palindrome function recursively here
    if left is None and right is None:
        return is_palindrome_recursive(text.lower(), 0, len(text) - 1)
    if right - left < 1:
        return True
    # Can do while loops for checking if characters in string
    if text[left] not in string.ascii_lowercase:
        return is_palindrome_recursive(text, left + 1, right)
    if text[right] not in string.ascii_lowercase:
        return is_palindrome_recursive(text, left, right - 1)
    if text[left] != text[right]:
        return False
    return is_palindrome_recursive(text, left + 1, right - 1)
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    # main()
    is_palindrome_recursive('')
