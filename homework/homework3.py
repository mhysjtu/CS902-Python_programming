# -*- coding: cp936 -*-
# Homework 3


##1.布尔运算
#(1)False
#(2)False
#(3)True
#(4)False


##2.硬币筛分器
print "Problem 2:"
a = raw_input("请输入一系列硬币值(1,5,10):")
b = a.split(",")
count1, count5, count10 = 0, 0, 0
for i in b:
    if int(i)==1:
        count1 = count1 + 1
    if int(i)==5:
        count5 = count5 + 1
    if int(i)==10:
        count10 = count10 + 1
print "\n硬币种类及个数为："
print "10" + "\t" + str(count10)
print "5" + "\t" + str(count5)
print "1" + "\t" + str(count1)


##3.判断闰年
print "\nProblem 3:"
year = raw_input("请输入一个年份：")
print "结果为："
if int(year) % 400 == 0:
    print year + "\t", 'Y'
elif int(year) % 4 == 0:
    if int(year) % 100 == 0:
        print year + '\t', 'N'
    if int(year) % 100 != 0:
        print year + "\t", 'Y'
else:
    print year + '\t', 'N'
    

##4.程序流程图
#(1)1. x-3<0 ?
#   2. y = x-3
#(2)1. r == 0 ?


##5.格式化输出
#(1)
print "\nProblem 5:"
print "\n1).1234格式化输出："
print "%8d" % 1234
print "%-8d" % 1234
print "%08d" % 1234
print "%-8d" % 1234
#(2)
print "\n2).1234.5678格式化输出："
print "%-10.4f" % 1234.5678
print "%10.6f" % 1234.5678
print "%10.3f" % 1234.5678
print "%10.6e" % 1234.5678
print "%10.5f" % 1234.5678
#(3)
print "\n3).字符串格式化输出："
str = "strong formatting"
print "%.15s" % str.capitalize()

for i in "%.5s  " % str.capitalize():
    print "%s " %i ,
