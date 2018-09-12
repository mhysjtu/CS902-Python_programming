# Homework 2


##1.Simple math
print 'Problem 1 :',
#a)
print '\n1.a):'
print 35.27 * 1.15 / 3

#b)
print '\n1.b):'
print 'Area =', 12.5 * 16.7
print 'Perimeter =', 2 * (12.5 + 16.7)

#c£©
import math
print '\n1.c):'
print 'Area =', math.pi * 50 * 50 / 4


##2.Convert temperatures
print '\nProblem 2 :'
x= input('Give a Fahrenheit degree : ')
print 'Fahrenheit is :', x, 'F'
result = 5/9.0*(x-32)
print 'Celsius is :', result, 'C'


##3.Convert Datatype
print '\nProblem 3 :'
x = input("Please input a dec string number : ")
result = int(bin(int(x))[2:])
print 'The bin number is :', result
