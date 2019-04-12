# -*- coding: utf-8 -*-

#Write a program that prints the number of times the string 'bob' occurs in s.
s = 'azcbobobegghakl'
count = 0
for x in range(len(s)):
     if s[x:x+3] == 'bob':
         count += 1
print(count)