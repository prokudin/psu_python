# -*- coding: utf-8 -*-

#Write a program that counts up the number of vowels contained in the string s.
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
s = 'azcbobobegghakl'
count=0

for letter in s:

    if(letter=='a' or letter == 'e' or letter =='i' or letter =='o' or letter=='u'):
         count=count+1

print(count)