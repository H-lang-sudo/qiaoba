#coding=gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ��ֱ���
���ڣ�2019.11.14
"""




def name_to_number(n):
    if n=="rock":
        return 0
    elif n=="Spock":
        return 1
    elif n=="paper":
        return 2
    elif n=="lizard":
        return 3
    elif n=="scissors":
        return 4
    else:
        print("Error: No Correct Name")
    return(n)
    
import random
a=random.randint(1,4)  
def number_to_name(a):
    if a==0:
        return "rock"
    elif a==1:
        return "Spock"
    elif a==2:
        return "paper"
    elif a==3:
        return "lizard"
    else:
        return "scissors"      
    return(a)

def rpsls(player_choice):
	player_choice_number = name_to_number(player_choice)   
	com_choice = number_to_name(a)
	print("����ѡ����%s"%player_choice)
	print("�������ѡ��Ϊ%s"%com_choice)
	if player_choice_number==0 and a==1:
		print("�����Ӯ��")
	elif player_choice_number==0 and a==2:
		print("�����Ӯ��")
	elif player_choice_number==0 and a==3:
		print("��Ӯ��")
	elif player_choice_number==0 and a==4:
		print("��Ӯ��")
	elif player_choice_number==1 and a==0:
		print("��Ӯ��")
	elif player_choice_number==1 and a==2:
		print("��Ӯ��")
	elif player_choice_number==1 and a==3:
		print("�����Ӯ��")
	elif player_choice_number==1 and a==4:
		print("��Ӯ��")
	elif player_choice_number==2 and a==0:
		print("��Ӯ��")
	elif player_choice_number==2 and a==1:
		print("��Ӯ��")
	elif player_choice_number==2 and a==3:
		print("�����Ӯ��")
	elif player_choice_number==2 and a==4:
		print("�����Ӯ��")
	elif player_choice_number==3 and a==0:
		print("�����Ӯ��")
	elif player_choice_number==3 and a==1:
		print("��Ӯ��")
	elif player_choice_number==3 and a==2:
		print("��Ӯ��")
	elif player_choice_number==3 and a==4:
		print("�����Ӯ��")
	elif player_choice_number==4 and a==0:
		print("�����Ӯ��")
	elif player_choice_number==4 and a==1:
		print("�����Ӯ��")
	elif player_choice_number==4 and a==2:
		print("��Ӯ��")
	elif player_choice_number==4 and a==3:
		print("��Ӯ��")
	else:
		print("���ͼ����һ����")
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
player_choice=input()
rpsls(player_choice)
