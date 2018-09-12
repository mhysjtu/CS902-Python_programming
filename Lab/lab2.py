import csv
import random

csv_reader=csv.reader(open('lab2.csv'))
print csv_reader

tmp=[]
for i in csv_reader:
    tmp.append(i)
tmp.remove(tmp[0])

stu=[]
for j in range(len(tmp)):
    if len(tmp[j])==1:
        stu.append(tmp[j])
        
new=[]
for k in stu:
    new.append((k,random.randint(0,100)))

numberOfstu=[0,0,0,0,0,0,0,0,0,0]

for k in new:
    if k[1]>=0 and k[1]<10:
        numberOfstu[0]=numberOfstu[0]+1
    if k[1]>=10 and k[1]<20:
        numberOfstu[1]=numberOfstu[1]+1
    if k[1]>=20 and k[1]<30:
        numberOfstu[2]=numberOfstu[2]+1
    if k[1]>=30 and k[1]<40:
        numberOfstu[3]=numberOfstu[3]+1
    if k[1]>=40 and k[1]<50:
        numberOfstu[4]=numberOfstu[4]+1
    if k[1]>=50 and k[1]<60:
        numberOfstu[5]=numberOfstu[5]+1
    if k[1]>=60 and k[1]<70:
        numberOfstu[6]=numberOfstu[6]+1
    if k[1]>=70 and k[1]<80:
        numberOfstu[7]=numberOfstu[7]+1
    if k[1]>=80 and k[1]<90:
        numberOfstu[8]=numberOfstu[8]+1
    if k[1]>=90 and k[1]<100:
        numberOfstu[9]=numberOfstu[9]+1

import matplotlib.pyplot as plt
import numpy as np

num=len(numberOfstu)
index = np.arange(num)
bar_width = 0.9

plt.bar(index,numberOfstu,bar_width,color='b',label='515020910125')
plt.xlabel('Grades')
plt.ylabel('Num of Students')
plt.title('No.515020910125')
plt.xticks(index-0.5+bar_width/2,('0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100',))
plt.show()
