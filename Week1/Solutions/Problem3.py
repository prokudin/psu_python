# -*- coding: utf-8 -*-

#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
s = 'azcbobobegghakl'
a = s[0]
b = s[0]
for c in s[1:]:
    if c >= b[-1]:
        b += c
        if len(b) > len(a):
            a = b
    else:
        b = c
print ("Longest substring in alphabetical order is:", a)