# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 20:43:50 2018

@author: Wilson
"""

dic1 = dict([["香蕉",20], ["蘋果", 40], ["百香果", 10] ])
print(dic1)
print(dic1["蘋果"])
print(len(dic1))


dicblood = {"A":"內向穩重", "B":"外向樂觀", "O":"堅強自信", "AB":"聰明自然"}
"""blood = input("請輸入查詢的血型:")"""
blood= "A"
final = dicblood.get(blood)
print(final)


dic2 = dicblood
print(dic2)

"""del dic2["O"]"""
print(dic2.keys())
print(dic2.values())
print("A" in dic2)
print("AB" in dicblood)
items = dic2.items()
print(items)

listitem = list(items)
print(listitem)


