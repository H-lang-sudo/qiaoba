#coding=gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ��ֱ���
���ڣ�2019.11.14
"""
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
name=input()



def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
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
    print("�����Ӯ��")
elif name=="rock" and a==2:
    print("�����Ӯ��")
elif name=="rock" and a==3:
    print("��Ӯ��")
elif name=="rock" and a==4:
    print("��Ӯ��")
elif name=="Spock" and a==0:
    print("��Ӯ��")
elif name=="Spock" and a==2:
    print("��Ӯ��")
elif name=="Spock" and a==3:
    print("�����Ӯ��")
elif name=="Spock" and a==4:
    print("��Ӯ��")
elif name=="paper" and a==0:
    print("��Ӯ��")
elif name=="paper" and a==1:
    print("��Ӯ��")
elif name=="paper" and a==3:
    print("�����Ӯ��")
elif name=="paper" and a==4:
    print("�����Ӯ��")
elif name=="lizard" and a==0:
    print("�����Ӯ��")
elif name=="lizard" and a==1:
    print("��Ӯ��")
elif name=="lizard" and a==2:
    print("��Ӯ��")
elif name=="lizard" and a==4:
    print("�����Ӯ��")
elif name=="scissors" and a==0:
    print("�����Ӯ��")
elif name=="scissors" and a==1:
    print("�����Ӯ��")
elif name=="scissors" and a==2:
    print("��Ӯ��")
elif name=="scissors" and a==3:
    print("��Ӯ��")
else:
    print("���ͼ����һ����")


