#!python

import math

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if index > len(array) - 1:
        return None
    elif item == array[index]:
        return index
    else:
        return linear_search_recursive(array, item, index + 1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    right = len(array) - 1
    left = 0
    index = (right + left) // 2

    while array[index] != item and right != left:
        if item < array[index]:
            right = index
            if right - left == 1:
                right = left
        else:
            left = index
            if right - left == 1:
                left = right

        index = math.ceil((right + left) / 2)

    if array[index] == item:
        return index
    else:
        return None
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # Starting recursive loop using passed in array to calculate 'right'
    if left is None:
        return binary_search_recursive(array, item, 0, len(array) - 1)

    if array[left] == item:
        return left
    elif array[right] == item:
        return right
    elif right - left == 1:
        return None

    index = (right + left) // 2
    if item < array[index]:
        return binary_search_recursive(array, item, left, index)
    else:
        return binary_search_recursive(array, item, index, right)
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
