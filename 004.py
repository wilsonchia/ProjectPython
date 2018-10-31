# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 14:59:31 2018

@author: Wilson
"""

total = n = 0
while(n<100):
    n +=1
    total += n
    print(total)
    
total = i = 1
n = int(input("請輸入正整數: "))
while(i<=n):
    total *=i
    i+=1
    print(total)
