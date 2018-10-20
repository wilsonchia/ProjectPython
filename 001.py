# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 06:49:41 2018

@author: Wilson
"""

num1 = 34
num2 = 67.83
print(num1 + num2)

str1 = "這是字串"
str2 = "小明說:你好!!"
str3 = "小華說:早安!!"

print(str1 + "\n" + str2 + "\n" + str3)

# Type命令 取得內容的資料型態
print(type(56))     #int
print(type(56.0))   #float
print(type(True))   #bool

#num2 = 223 + "67"
num3 = 23 + int("67")
print(num3)

score = 60
print("score is " + str(score))

name = "曉明"
score = 80
print("%s 的成績是 %d" % (name, score))

print("{} 的成績是 {}".format(name,score))

score = input("請輸入數學成績 : ")
print("數學成績是" + score)
if (int(score) > 60):
    print("\n及格")
else:
    print("\n不及格")


chinese = input("輸入國文成績: ")
math = input("輸入數學成績: ")
english = input("輸入英文成績: ")
total = int(chinese) + int(math) + int(english)
average = total / 3
print("成績總和是 {}".format(total))
print("成績平均是 {}".format(average))


desposit = int(input("請輸入本金金額: "))
times = 1.02 ** 6
desposit *= times
print(" 6 年存款為{}".format(str(desposit)))
