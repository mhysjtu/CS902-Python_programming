# -*- coding: cp936 -*-

##形态学方法解特定迷宫的算法实现

from random import *
import cv2
import numpy as np

class Maze:
    def __init__(self, total):
        self.num = 0
        self.total = total
        
    ##从文件夹中随机选取一个迷宫，并做转为GUI前的预处理
    def randomMap(self):
        self.num = randrange(1, self.total)
        filename = "mazes\\maze" + str(self.num) + ".png"
        print "You've chosen "+filename
        
        img = cv2.imread(filename)
        ##RGB转灰度图
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ##二值化
        bin_img  = cv2.threshold(gray_img, 1, 255, cv2.THRESH_BINARY)
        mat = bin_img[1]
        return mat, self.num

    ##求解迷宫的答案
    def mazeAnswer(self):
        filename = "mazes\\maze" + str(self.num) + ".png"
        
        img = cv2.imread(filename)
        ##RGB转灰度图
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ##二值化
        binary_img = cv2.threshold(gray_img, 1, 255, cv2.THRESH_BINARY_INV)
        ##找出边界
        contours = cv2.findContours(binary_img[1], cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        h,w,d = img.shape
        path = np.zeros((h ,w), dtype = np.uint8)

        ##画出边界
        cv2.drawContours(path, contours[0], 0, (255,255,255), -1)

        ##设定一个卷积核
        kernel = np.ones((25,25), dtype = np.uint8)

        ##膨胀操作
        dilate = cv2.dilate(path,kernel)
        ##对膨胀后的再进行侵蚀
        erosion = cv2.erode(dilate, kernel)
        ##取膨胀和侵蚀的绝对差值，即得出迷宫的解
        path_diff = cv2.absdiff(dilate, erosion)

        return path_diff
