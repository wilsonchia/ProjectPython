# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 07:21:28 2018

@author: Wilson
"""

"""
pw = input("請輸入密碼: ")
if (pw == "1234" ) : 
    print("歡迎光臨")
else :
    print("密碼錯誤")
    
score = input("請輸入成績: ")    
if (int(score) >= 90):
    print("優等")
elif (int(score) >= 80) :
    print("甲等")
elif (int(score) >= 70) :
    print("乙等")
elif (int(score) >= 60) :
    print("丙等")
else :
    print("丁等")


money = int(input("請輸入購物金額: "))
showMess = ""
if (money >= 10000) :
    if (money >= 100000) :
        showMess = str(money * 0.8)
    elif (money >= 70000) :
        showMess = str(money * 0.85)
    elif (money >= 60000) :
        showMess = str(money * 0.9)
    elif (money >= 50000) :
        showMess = str(money * 0.95)
else :
    showMess = money
print(showMess + "  元\n")
"""

#Range

list1 = range(5)
print(list(list1))
list2 = range(-3,8)
list3 = range(2,22)
list4 = range(2,34,2)
list5 = range(1,15,2)
print(list(list2))
print(list(list3))
print(list(list4))
print(list(list5))


for n in range(5):
    print(n,end=",")
    

n = int(input("請輸入正整數 : "))
for i in range(1,n+1):
    print(i, end= ",")
    
sum = 0
n = int(input("請輸入正整數: "))    
for i in range(1, n+1):
    sum += i
print(" 1 到 %d 的整數和 %d " % (n,sum))

