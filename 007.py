# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 20:59:42 2018

@author: Wilson
"""


"""
自定函數
"""

def Sayhello():
    print(" Hello!!")
    
Sayhello()


def GetArea(width, height) :
    area = width * height
    return area

print(GetArea(150,500))


def Circle(radius):
    area = radius * radius * 314 
    length = 2 * radius * 3.14
    return area, length

print(Circle(500))


def ctof(c):
    f = c * 1.8 + 32
    return f

print(ctof(28))


"""
    預設參數值要放在最後 不能放在前面
"""
def GetArea(width, height=20) :
    return width * height

print(GetArea(50))

print(GetArea(55,75))


"""
    global 設定變數為全域變數
"""
def scope():
    global val1
    val1 = 50
    print(val1, val2)
    
val1 = 100
val2 = 20
print(val1, val2)
scope()
print(val1,val2)


"""
pow       取得餘數
divmod    求餘數    同時傳回商數和餘數
round     四捨五入
"""
repow = pow(44, 7, 3)
print(repow)
redivmod = divmod(44,7)
print(redivmod)
reround = round(44.6)
print(reround)

"""
max 最大數
min 最小數
sum 加總
sorted 排序   reserve = True / False
"""

list1 = { 4,50,39,199}
print(max(list1))
print(min(list1))
print(sum(list1))
list2 = list1
print(list2)
print(list2.copy())
print(sorted(list2))
print(sorted(list2, reverse=True))


"""
字串函式處理
center(n)   將字串擴充為n個字元並置中
find(s)     搜尋該字元在第幾個位置
endswith(s) 是否以s字元字串結尾    True / False
startwith(s)是否以s字元字串開頭    True / False
islower()   是否都是小寫字母
isupper()   是否都是大寫字母
lower()     全部改為小寫字母
upper()     全部改為大寫字母
replace()
"""
strWord = "This a Sample Word"
print(strWord.center(40))
print(strWord.find('o'))
print(strWord.endswith('s'))
print(strWord.startswith('s'))
print(strWord.islower())
print(strWord.isupper())
print(strWord.lower())
print(strWord.upper())
print(strWord.replace('a','n'))





