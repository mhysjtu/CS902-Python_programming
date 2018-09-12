# -*- coding: cp936 -*-
#homework_4

print "第1题："
##1.简单循环
while True:
    f = input("请输入起始的f：")
    t = input("请输入终止的t：")
    i = input("请输入增量i：")
    if(f > t or i < 0):
        print "请重新输入，确保f小于t且i为正值！"
    else:
        break
print "所得数列为："
for j in range(f, t+1, i):
    print j,
print "\n"




while True:
    a = raw_input("下一题？（直接回车）")
    if a == "":
        break


    
print "第2题："
##2.猜数字
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
    a = raw_input("下一题？（直接回车）")
    if a == "":
        break
    


print "第3题："
##3.打印乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print str(j) + "x" + str(i) + "=" + str(i*j) + "\t",
    print "\n"



while True:
    a = raw_input("下一题？（直接回车）")
    if a == "":
        break




print "第4题："
##4.比特操作
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
    a = raw_input("下一题？（直接回车）")
    if a == "":
        break



print "第5题："
##5.while循环和for循环
###3_10.py
print "3-10："
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
print "3-11："
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
print "3-12："
sum = 0
for i in range(1000):
    x = raw_input("Input a number (<Enter> to quit):")
    if x == "":
        break
    else:
        sum = sum + eval(x)
print "The sum is", sum



while True:
    a = raw_input("下一题？（直接回车）")
    if a == "":
        break



print "第六题："
##6.完善德州扑克游戏

##程序说明：
##1.只能单人或两人游戏
##2.能分辨十种牌的类型，但是同一类牌不能分出大小
##3.全部牌型列在test处，若需检查能否全部准确识别，取消注释即可

import random


#初始化
#设置初始值
def initial():
    global if_straight
    global if_flush
    global max_straight
    if_straight = False
    if_flush = True
    max_straight = False


#生成n副扑克牌并洗牌
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


#单人游戏发5张牌
def NewHand1(cards):
    global player1
    player1 = cards[:5]
    return player1

#两人游戏，每人发五张
def NewHand2(cards):
    global player1
    global player2
    player1 = cards[0:5]
    player2 = cards[5:10]
    return player1, player2


#手牌排序
#输入：得到的洗过的手牌
#输出：手牌排好序后的一组数字
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



#判断是否是顺子
#输入：手牌排好序后的数组
#输出：无输出，改变if_straight的值
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
    print "有无顺子？:\t", if_straight



#判断是否是同花
#输入：洗过的手牌
#输出：无输出，改变if_flush的值
def IfFlush(newhand):
    global if_flush
    suit = []
    for i in range(0, len(newhand)):
        suit.append(newhand[i][1])
    
    for j in range(0, len(suit)-1):
        if suit[j] != suit[j+1]:
            if_flush = False
            break
    print "有无同花？:\t", if_flush


#判断有几张相同的牌
#输入：手牌排好序后的数组
#输出：相同的牌数（1：一对；2：两对；3：俘虏；4：葫芦；6：炸）
def IfSame(hand):
    TrueNum = 0
    for i in range(0, len(hand)-1):
        for j in range(i+1, len(hand)):
            if hand[i]==hand[j]:
                TrueNum = TrueNum +1
    return TrueNum


#判断牌型大小
#输入:手牌
#输出：牌型及大小顺序1：10
def WhichType(hand):
    
    initial()
    print "你的手牌为：\n", hand
    
    rank = RangeHand(hand)
    print "整理后牌的大小为：", rank
    
    num = 0
    same_num = IfSame(rank)
    
    IfStraight(rank)
    IfFlush(hand)
    print "震惊了！拿到的居然是：",
    if max_straight and if_flush:
        print "\n皇家同花顺！！！最大！！"
        num = 10
    elif if_straight and if_flush:
        print "\n同花顺！！"
        num = 9
    elif same_num == 6:
        print "\n四条！！"
        num = 8
    elif same_num == 4:
        print "\n葫芦！！"
        num = 7
    elif (not if_straight) and if_flush:
        print "\n同花！"
        num = 6
    elif if_straight and (not if_flush):
        print "\n顺子！"
        num = 5
    elif same_num == 3:
        print "\n三条！"
        num = 4
    elif same_num == 2:
        print "\n两对"
        num = 3
    elif same_num == 1:
        print "\n一对"
        num = 2
    else:
        print "\n高牌"
        num = 1
        
    print "拿到的分数:\t", num, "\n"
    return num



#判断谁赢
#输入：玩家num
#输出：谁赢
def WhoWin(num1, num2):
    print "游戏结果："
    if num1 > num2:
        print "玩家1获胜！"
    elif num1 < num2:
        print "玩家2获胜！"
    else:
        print "平局！"




###开始游戏

###单人游戏
print "#########\n单人游戏：\n#########"
a = CreateCards()
player1 = []
NewHand1(a)
print "***************"
print "玩家1！"
print "***************\n"
WhichType(player1)

while True:
    a = raw_input("想玩两人游戏？（是则直接回车）")
    if a == "":
        break
    else:
        print "玩玩嘛！"

###两人游戏
print "#########\n两人游戏: \n#########"
a = CreateCards()
player1 = []
player2 = []
NewHand2(a)
print "***************"
print "玩家1！"
print "***************\n"
num1 = WhichType(player1)
print "***************"
print "玩家2！"
print "***************\n"
num2 = WhichType(player2)
WhoWin(num1, num2)


###test:
a = raw_input("\n想测试全部牌型？(是则按回车)")
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
        print "测一下呗"














