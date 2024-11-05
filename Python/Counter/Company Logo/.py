#!/bin/python3
#  T -> O(N)

import math
import os
import random
import re
import sys

def sort_by_occurence(s):
    dict = {}
    for char in s:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    
    freq_dict = sorted(dict.items(), key=lambda x: (-x[1], x[0]))
    
    for ch, freq in freq_dict[:3]:
        print(f"{ch} {freq}")


if __name__ == '__main__':
    s = input()
    sort_by_occurence(s)
