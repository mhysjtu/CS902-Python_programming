# -*- coding: cp936 -*-

##迷宫游戏界面的实现

from Tkinter import *
from tkMessageBox import *

class gui:
    def __init__(self,mat,numOfMaze):
        self.width = 15
        self.x = 41
        self.y = 41
        self.mat = mat
        self.numOfMaze = numOfMaze

        ##机器人的初始位置参数
        self.start_row = 0
        self.start_column = 0
        self.end_row = 0
        self.end_column = 0
        self.robotPos =[]
        
        self.num = 0
        self.row = []
        self.column = []
        
        self.numans = 0
        self.rowans = []
        self.columnans = []

        ##障碍
        self.buildings = []
        ##答案的路径
        self.answer = []
        ##经过的路
        self.passed = []
        
        self.window = Tk()
        self.window.title("Maze")

        self.label = Label(self.window, text = "")
        self.label.grid(row = 0,column = 0)
        
        self.view = Canvas(self.window, width = self.x * self.width,
                                        height = self.y * self.width)
        self.view.grid(row = 1, column = 0)

        self.f = Frame(self.window, bd = 4, relief = "groove")
        self.f.grid(row = 2, column = 0)
        
        self.b = Button(self.f, text = "I give up! Give me the answer!", command = self.drawAnswer)
        self.b.grid(row = 0, column = 0)
        
        self.restart = Button(self.f, text = "Restart!", command = self.Restart)
        self.restart.grid(row = 0, column = 1)

        self.window.bind("<Up>",self.move_up)
        self.window.bind("<Down>",self.move_down)
        self.window.bind("<Right>",self.move_right)
        self.window.bind("<Left>",self.move_left)
        self.window.focus_set()

        self.window.protocol("WM_DELETE_WINDOW",self.callback)

        
    ##将处理过的图片矩阵转为迷宫中障碍物的矩阵
    def generateBuildings(self):
        print "generating..."
        for i in range(1, 321, 8):
            for j in range(1, 321, 8):
                if self.mat[i][j] == 0:
                    self.num = self.num + 1
                    a = (j-1)/8
                    b = (i-1)/8
                    self.row.append(a)
                    self.column.append(b)
                elif i == 1:
                    self.start_row = (j-1)/8
                    self.start_column = (i-1)/8
        for j in range(1, 321, 8):
            if self.mat[320][j] == 0:
                self.num = self.num + 1
                a = (j-1)/8
                b = 40
                self.row.append(a)
                self.column.append(b)
            else:
                self.end_row = (j-1)/8
                self.end_column = 40
        
        for i in range(self.num):
            self.buildings.append((self.row[i],self.column[i]))
        for i in range(40):
            self.buildings.append((40,i))
        self.buildings.append((40,40))

        #print self.buildings

    ##生成答案路径的矩阵
    def generateAnswer(self, matans):
        for i in range(1, 321, 8):
            for j in range(1, 321, 8):
                if matans[i][j] == 255:
                    self.numans = self.numans + 1
                    c = (j-1)/8
                    d = (i-1)/8
                    self.rowans.append(c)
                    self.columnans.append(d)
        for j in range(1, 321, 8):
            if matans[320][j] == 255:
                self.numans = self.numans + 1
                c = (j-1)/8
                d = 40
                self.rowans.append(c)
                self.columnans.append(d)

        for i in range(self.numans):
            self.answer.append((self.rowans[i], self.columnans[i]))
            
    ##根据障碍物矩阵画出迷宫
    def drawMaze(self):
        self.label.config(text="Maze"+str(self.numOfMaze)+":")
        for i in range(self.x):
            for j in range(self.y):
                self.view.create_rectangle(i * self.width, j * self.width, (i + 1) * self.width, (j + 1) * self.width,fill='white', outline='gray', width=2)
            for (i, j) in self.buildings:
                self.view.create_rectangle(i * self.width, j * self.width, (i + 1) * self.width, (j + 1) * self.width,fill='black', outline='gray', width=2)

    ##画出机器人的初始位置
    def drawRobot(self):
        self.robotPos = [self.start_row, self.start_column]
        self.view.create_rectangle(self.robotPos[0] * self.width + self.width * 2 / 10, self.robotPos[1] * self.width + self.width * 2 / 10,
                                   self.robotPos[0] * self.width + self.width * 8 / 10, self.robotPos[1] * self.width + self.width * 8 / 10,fill="blue", width=1, tag="robot")

    ##根据答案路径的矩阵画出答案
    def drawAnswer(self):
        self.label1 = Label(self.window, text = "Answer:")
        self.label1.grid(row = 0, column = 1)
        view_ans = Canvas(self.window, width=self.x * self.width, height=self.y * self.width)
        view_ans.grid(row=1, column=1)
        for i in range(self.x):
            for j in range(self.y):
                view_ans.create_rectangle(i * self.width, j * self.width, (i + 1) * self.width, (j + 1) * self.width,fill='white', outline='gray', width=2)
                
        for (i, j) in self.buildings:
            view_ans.create_rectangle(i * self.width, j * self.width, (i + 1) * self.width, (j + 1) * self.width,fill='black', outline='gray', width=2)

        for (i, j) in self.answer:
            view_ans.create_rectangle(i * self.width, j * self.width, (i + 1) * self.width, (j + 1) * self.width,fill='red', outline='gray', width=2)
            
    ##清楚已走过的路径，让游戏重新开始
    def Restart(self):
        print "Restarting......"
        self.view.delete("all")
        self.passed = []
        self.robotPos[0] = self.start_row
        self.robotPos[1] = self.start_column

        self.drawMaze()
        self.drawRobot()

        print "Restarted!!"

    ##向上移动机器人
    def move_up(self,event):
        #print "Up",self.robotPos[0],self.robotPos[1]
        self.robotPos[1]=self.robotPos[1]-1
        ##防止碰墙或走回头路的判断条件，下同
        if not((self.robotPos[0],self.robotPos[1]) in self.buildings) and not((self.robotPos[0],self.robotPos[1]) in self.passed):
            robot = self.view.create_rectangle(self.robotPos[0] * self.width + self.width * 2 / 10, self.robotPos[1] * self.width + self.width * 2 / 10,
                              self.robotPos[0] * self.width + self.width * 8 / 10, self.robotPos[1] * self.width + self.width * 8 / 10, fill="blue", width=1, tag="robot")
            self.passed.append((self.robotPos[0],self.robotPos[1]))
        else:
            print "?"
            self.robotPos[1]=self.robotPos[1]+1
        ##判断是否进入死胡同，即是否输掉，下同
        if ((self.robotPos[0],self.robotPos[1]-1) in self.buildings) and ((self.robotPos[0]+1,self.robotPos[1]) in self.buildings) and ((self.robotPos[0]-1,self.robotPos[1]) in self.buildings) and ((self.robotPos[0],self.robotPos[1]+1) in self.passed):
            top = Toplevel()
            Label(top,text="LOL You Lose!!!\nClick restart button to play again!!").pack()

    ##向下移动机器人
    def move_down(self,event):
        #print "down",robotPos[0],robotPos[1]
        self.robotPos[1]=self.robotPos[1]+1
        if not((self.robotPos[0],self.robotPos[1]) in self.buildings) and not((self.robotPos[0],self.robotPos[1]) in self.passed):
            robot = self.view.create_rectangle(self.robotPos[0] * self.width + self.width * 2 / 10, self.robotPos[1] * self.width + self.width * 2 / 10,
                          self.robotPos[0] * self.width + self.width * 8 / 10, self.robotPos[1] * self.width + self.width * 8 / 10, fill="blue", width=1, tag="robot")
            self.passed.append((self.robotPos[0],self.robotPos[1]))
        else:
            print "?"
            self.robotPos[1]=self.robotPos[1]-1
        if ((self.robotPos[0],self.robotPos[1]+1) in self.buildings) and ((self.robotPos[0]+1,self.robotPos[1]) in self.buildings) and ((self.robotPos[0]-1,self.robotPos[1]) in self.buildings) and ((self.robotPos[0],self.robotPos[1]-1) in self.passed):
            top = Toplevel()
            Label(top,text="LOL You Lose!!!\nClick restart button to play again!!").pack()
        ##判断是否胜利
        if (self.end_row,self.end_column) in self.passed:
            top = Toplevel()
            Label(top,text="Congratulations!!\nYou win!!\nWhat a genius!").pack()

    ##向左移动机器人  
    def move_left(self,event):
        #print "left"
        self.robotPos[0]=self.robotPos[0]-1
        if not((self.robotPos[0],self.robotPos[1]) in self.buildings) and not((self.robotPos[0],self.robotPos[1]) in self.passed):
            robot = self.view.create_rectangle(self.robotPos[0] * self.width + self.width * 2 / 10, self.robotPos[1] * self.width + self.width * 2 / 10,
                          self.robotPos[0] * self.width + self.width * 8 / 10, self.robotPos[1] * self.width + self.width * 8 / 10, fill="blue", width=1, tag="robot")
            self.passed.append((self.robotPos[0],self.robotPos[1]))
        else:
            print "?"
            self.robotPos[0]=self.robotPos[0]+1
        if ((self.robotPos[0],self.robotPos[1]-1) in self.buildings) and ((self.robotPos[0],self.robotPos[1]+1) in self.buildings) and ((self.robotPos[0]+1,self.robotPos[1]) in self.passed) and ((self.robotPos[0]-1,self.robotPos[1]) in self.buildings):
            top = Toplevel()
            Label(top,text="LOL You Lose!!!\nClick restart button to play again!!").pack()

    ##向右移动机器人 
    def move_right(self,event):
        #print "right"
        self.robotPos[0]=self.robotPos[0]+1
        if not((self.robotPos[0],self.robotPos[1]) in self.buildings) and not((self.robotPos[0],self.robotPos[1]) in self.passed):
            robot = self.view.create_rectangle(self.robotPos[0] * self.width + self.width * 2 / 10, self.robotPos[1] * self.width + self.width * 2 / 10,
                          self.robotPos[0] * self.width + self.width * 8 / 10, self.robotPos[1] * self.width + self.width * 8 / 10, fill="blue", width=1, tag="robot")
            self.passed.append((self.robotPos[0],self.robotPos[1]))
        else:
            print "?"
            self.robotPos[0]=self.robotPos[0]-1
        if ((self.robotPos[0],self.robotPos[1]-1) in self.buildings) and ((self.robotPos[0]+1,self.robotPos[1]) in self.buildings) and ((self.robotPos[0]-1,self.robotPos[1]) in self.passed) and ((self.robotPos[0],self.robotPos[1]+1) in self.buildings):
            top = Toplevel()
            Label(top,text="LOL You Lose!!!\nClick restart button to play again!!").pack()

    ##关闭窗口给予提示
    def callback(self):
        if askokcancel("Quit","Such an interesting game! Do you really wish to quit???"):
            self.window.destroy()

    ##执行窗口事件
    def run(self,matans):
        self.generateBuildings()
        self.generateAnswer(matans)
        self.drawMaze()
        self.drawRobot()
        
        self.window.mainloop()
        
        




