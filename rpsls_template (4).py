#coding=gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：林冰清
日期：2019.11.14
"""
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
name=input()



def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name=="rock":
        name==0
    elif name=="Spock":
        name==1
    elif name=="paper":
        name==2
    elif name=="lizard":
        name==3
    elif name=="scissors":
        name==4
    else:
        print("Error: No Correct Name")
name_to_number(name)
   
import random
a=random.randint(1,4)   
def number_to_name(a):
    if a==0:
        print("rock")
    elif a==1:
        print("Spock")
    elif a==2:
        print("paper")
    elif a==3:
        print("lizard")
    else:
        print("scissors")
number_to_name(a)


    
   
if name=="rock" and a==1:
    print("计算机赢了")
elif name=="rock" and a==2:
    print("计算机赢了")
elif name=="rock" and a==3:
    print("您赢了")
elif name=="rock" and a==4:
    print("您赢了")
elif name=="Spock" and a==0:
    print("您赢了")
elif name=="Spock" and a==2:
    print("您赢了")
elif name=="Spock" and a==3:
    print("计算机赢了")
elif name=="Spock" and a==4:
    print("您赢了")
elif name=="paper" and a==0:
    print("您赢了")
elif name=="paper" and a==1:
    print("您赢了")
elif name=="paper" and a==3:
    print("计算机赢了")
elif name=="paper" and a==4:
    print("计算机赢了")
elif name=="lizard" and a==0:
    print("计算机赢了")
elif name=="lizard" and a==1:
    print("您赢了")
elif name=="lizard" and a==2:
    print("您赢了")
elif name=="lizard" and a==4:
    print("计算机赢了")
elif name=="scissors" and a==0:
    print("计算机赢了")
elif name=="scissors" and a==1:
    print("计算机赢了")
elif name=="scissors" and a==2:
    print("您赢了")
elif name=="scissors" and a==3:
    print("您赢了")
else:
    print("您和计算机一样呢")


