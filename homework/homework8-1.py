# -*- coding: cp936 -*-
#仅适用于一位数字之间的运算
class Stack():
    def __init__(self):
        self.stack = []
        
    def push(self,x):
        self.stack.append(x)

    def pop(self):
        ele = self.stack[-1]
        self.stack = self.stack[:-1]
        return ele

    def isEmpty(self):
        return (self.stack == [])

def main():
    a = raw_input("Please enter a Reverse Polish Notation: ")
    
    stack=Stack()

    for i in range(len(a)):
        if a[i].isdigit():
            stack.push(a[i])
        else:
            stack.push(str(eval(stack.pop()+a[i]+stack.pop())))

    print 'The result is: '+stack.pop()      

if __name__=="__main__":
    main()
