# -*- coding: cp936 -*-
#homework_4

print "��1�⣺"
##1.��ѭ��
while True:
    f = input("��������ʼ��f��")
    t = input("��������ֹ��t��")
    i = input("����������i��")
    if(f > t or i < 0):
        print "���������룬ȷ��fС��t��iΪ��ֵ��"
    else:
        break
print "��������Ϊ��"
for j in range(f, t+1, i):
    print j,
print "\n"




while True:
    a = raw_input("��һ�⣿��ֱ�ӻس���")
    if a == "":
        break


    
print "��2�⣺"
##2.������
print "Hello! What is your name?"
name = raw_input("My name is:")
print "Well, " + name +", I am thinking of a number between 1 and 20."
import random
num = random.randint(1,20)
chance = 1
for i in range(1,7):
    print "Take your guess (" + str(i) + "):"
    guess = raw_input()
    if int(guess) == num:
        print "Good job," + name + "! You guessed my number in " + i + " guesses!"
        break
    elif i == 6:
        print "You lose!"
    else:
        print "Narrowly! Try again!"




while True:
    a = raw_input("��һ�⣿��ֱ�ӻس���")
    if a == "":
        break
    


print "��3�⣺"
##3.��ӡ�˷���
for i in range(1,10):
    for j in range(1,i+1):
        print str(j) + "x" + str(i) + "=" + str(i*j) + "\t",
    print "\n"



while True:
    a = raw_input("��һ�⣿��ֱ�ӻس���")
    if a == "":
        break




print "��4�⣺"
##4.���ز���
print "OUTPUT"
print "----------"
begin = raw_input("Enter begin value:\t")
end = raw_input("Enter end value:\t")
print "\nDEC\tBIN\t\tHEX"
print "--------------------------------"
for a in range(int(begin), int(end)+1):
    b = int(bin(a)[2:])
    print str(a) + "\t" + "%06d" %b + "\t\t%x" %a



while True:
    a = raw_input("��һ�⣿��ֱ�ӻس���")
    if a == "":
        break



print "��5�⣺"
##5.whileѭ����forѭ��
###3_10.py
print "3-10��"
sum = 0
moredata = "yes"
for i in range(1000):
    x = input("Input a number: ")
    sum = sum + x
    moredata = raw_input("More?(yes/no)")
    if moredata[0] != "y":
        break
print "The sum is", sum

###3_11.py
print "3-11��"
sum = 0
for i in range(1000):
    x = input("Input a number (-1 to quit): ")
    if x == -1:
        sum = 0
        break
    else:
        sum = sum + x
print "The sum is", sum

###3_12.py
print "3-12��"
sum = 0
for i in range(1000):
    x = raw_input("Input a number (<Enter> to quit):")
    if x == "":
        break
    else:
        sum = sum + eval(x)
print "The sum is", sum



while True:
    a = raw_input("��һ�⣿��ֱ�ӻس���")
    if a == "":
        break



print "�����⣺"
##6.���Ƶ����˿���Ϸ

##����˵����
##1.ֻ�ܵ��˻�������Ϸ
##2.�ֱܷ�ʮ���Ƶ����ͣ�����ͬһ���Ʋ��ֳܷ���С
##3.ȫ����������test�����������ܷ�ȫ��׼ȷʶ��ȡ��ע�ͼ���

import random


#��ʼ��
#���ó�ʼֵ
def initial():
    global if_straight
    global if_flush
    global max_straight
    if_straight = False
    if_flush = True
    max_straight = False


#����n���˿��Ʋ�ϴ��
def CreateCards(n = 1):
    cards = []
    for j in range(1, n + 1):
        for i in range(1, 14):
            cards.append((i, 'heart'))
            cards.append((i, 'clubs'))
            cards.append((i, 'diamond'))
            cards.append((i, 'spade'))
    random.shuffle(cards)
    return cards


#������Ϸ��5����
def NewHand1(cards):
    global player1
    player1 = cards[:5]
    return player1

#������Ϸ��ÿ�˷�����
def NewHand2(cards):
    global player1
    global player2
    player1 = cards[0:5]
    player2 = cards[5:10]
    return player1, player2


#��������
#���룺�õ���ϴ��������
#����������ź�����һ������
def RangeHand(new):
    num = []
    for i in range(0, len(new)):
        num.append(new[i][0])
    for i in range(1, len(num)):
        for j in range(len(num)-1, i-1, -1):
            if num[j]>num[j-1]:
                tmp = num[j]
                num[j] = num[j-1]
                num[j-1] = tmp
    return num



#�ж��Ƿ���˳��
#���룺�����ź���������
#�������������ı�if_straight��ֵ
def IfStraight(rangedhand):
    global if_straight
    global max_straight
    if rangedhand[4] == 1:
        if (rangedhand[0] == 13) and (rangedhand[1] == 12) and (rangedhand[2] == 11) and (rangedhand[3] == 10):
            if_straight = True
            max_straight = True
        else:
            if_straight = False
    else:
        if (rangedhand[0]-rangedhand[1])== 1 and (rangedhand[1]-rangedhand[2])== 1 and (rangedhand[2]-rangedhand[3])== 1:
            if_straight = True
        else:
            if_straight = False
    print "����˳�ӣ�:\t", if_straight



#�ж��Ƿ���ͬ��
#���룺ϴ��������
#�������������ı�if_flush��ֵ
def IfFlush(newhand):
    global if_flush
    suit = []
    for i in range(0, len(newhand)):
        suit.append(newhand[i][1])
    
    for j in range(0, len(suit)-1):
        if suit[j] != suit[j+1]:
            if_flush = False
            break
    print "����ͬ����:\t", if_flush


#�ж��м�����ͬ����
#���룺�����ź���������
#�������ͬ��������1��һ�ԣ�2�����ԣ�3����²��4����«��6��ը��
def IfSame(hand):
    TrueNum = 0
    for i in range(0, len(hand)-1):
        for j in range(i+1, len(hand)):
            if hand[i]==hand[j]:
                TrueNum = TrueNum +1
    return TrueNum


#�ж����ʹ�С
#����:����
#��������ͼ���С˳��1��10
def WhichType(hand):
    
    initial()
    print "�������Ϊ��\n", hand
    
    rank = RangeHand(hand)
    print "������ƵĴ�СΪ��", rank
    
    num = 0
    same_num = IfSame(rank)
    
    IfStraight(rank)
    IfFlush(hand)
    print "���ˣ��õ��ľ�Ȼ�ǣ�",
    if max_straight and if_flush:
        print "\n�ʼ�ͬ��˳��������󣡣�"
        num = 10
    elif if_straight and if_flush:
        print "\nͬ��˳����"
        num = 9
    elif same_num == 6:
        print "\n��������"
        num = 8
    elif same_num == 4:
        print "\n��«����"
        num = 7
    elif (not if_straight) and if_flush:
        print "\nͬ����"
        num = 6
    elif if_straight and (not if_flush):
        print "\n˳�ӣ�"
        num = 5
    elif same_num == 3:
        print "\n������"
        num = 4
    elif same_num == 2:
        print "\n����"
        num = 3
    elif same_num == 1:
        print "\nһ��"
        num = 2
    else:
        print "\n����"
        num = 1
        
    print "�õ��ķ���:\t", num, "\n"
    return num



#�ж�˭Ӯ
#���룺���num
#�����˭Ӯ
def WhoWin(num1, num2):
    print "��Ϸ�����"
    if num1 > num2:
        print "���1��ʤ��"
    elif num1 < num2:
        print "���2��ʤ��"
    else:
        print "ƽ�֣�"




###��ʼ��Ϸ

###������Ϸ
print "#########\n������Ϸ��\n#########"
a = CreateCards()
player1 = []
NewHand1(a)
print "***************"
print "���1��"
print "***************\n"
WhichType(player1)

while True:
    a = raw_input("����������Ϸ��������ֱ�ӻس���")
    if a == "":
        break
    else:
        print "�����"

###������Ϸ
print "#########\n������Ϸ: \n#########"
a = CreateCards()
player1 = []
player2 = []
NewHand2(a)
print "***************"
print "���1��"
print "***************\n"
num1 = WhichType(player1)
print "***************"
print "���2��"
print "***************\n"
num2 = WhichType(player2)
WhoWin(num1, num2)


###test:
a = raw_input("\n�����ȫ�����ͣ�(���򰴻س�)")
while True:
    if a == "":
        WhichType([(1, 'clubs'), (10, 'clubs'), (12, 'clubs'), (11, 'clubs'), (13, 'clubs')])
        WhichType([(6, 'clubs'), (10, 'clubs'), (7, 'clubs'), (9, 'clubs'), (8, 'clubs')])
        WhichType([(6, 'clubs'), (6, 'diamond'), (6, 'spade'), (9, 'diamond'), (6, 'diamond')])
        WhichType([(6, 'clubs'), (6, 'diamond'), (9, 'spade'), (9, 'diamond'), (6, 'diamond')])
        WhichType([(6, 'diamond'), (10, 'diamond'), (12, 'diamond'), (9, 'diamond'), (6, 'diamond')])
        WhichType([(6, 'clubs'), (5, 'diamond'), (4, 'spade'), (3, 'diamond'), (7, 'diamond')])
        WhichType([(6, 'clubs'), (5, 'diamond'), (9, 'spade'), (9, 'diamond'), (9, 'diamond')])
        WhichType([(6, 'clubs'), (10, 'diamond'), (10, 'spade'), (9, 'diamond'), (6, 'diamond')])
        WhichType([(6, 'clubs'), (10, 'diamond'), (12, 'spade'), (9, 'diamond'), (6, 'diamond')])
        WhichType([(1, 'clubs'), (13, 'diamond'), (12, 'spade'), (9, 'diamond'), (6, 'diamond')])
        break
    else:
        print "��һ����"














