# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 15:27:23 2018

@author: Wilson
"""


scores = [85,79,93]
print ("國文成績 : %d 分" % scores[0])
print ("英文成績 : %d 分" % scores[1])
print ("數學成績 : %d 分" % scores[2])

lists = ["香蕉", "蘋果", "梨子"]
for s in lists :
    print(s , end=",")
    
    
print(len(lists))

for i in range(len(lists)) :
    print(lists[i])
    
    
n = lists.index("蘋果")
print(n)

n = lists.count("香蕉")
print(n)

lists.append("鳳梨")

print(lists)

lists.insert(3,"葡萄")
print(lists)

lists.remove("鳳梨")
print(lists)

del lists[3]
print(lists)

lists.sort()
print(lists)


lists.reverse()
print(lists)

    
