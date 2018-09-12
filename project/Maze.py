# -*- coding: cp936 -*-

##��̬ѧ�������ض��Թ����㷨ʵ��

from random import *
import cv2
import numpy as np

class Maze:
    def __init__(self, total):
        self.num = 0
        self.total = total
        
    ##���ļ��������ѡȡһ���Թ�������תΪGUIǰ��Ԥ����
    def randomMap(self):
        self.num = randrange(1, self.total)
        filename = "mazes\\maze" + str(self.num) + ".png"
        print "You've chosen "+filename
        
        img = cv2.imread(filename)
        ##RGBת�Ҷ�ͼ
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ##��ֵ��
        bin_img  = cv2.threshold(gray_img, 1, 255, cv2.THRESH_BINARY)
        mat = bin_img[1]
        return mat, self.num

    ##����Թ��Ĵ�
    def mazeAnswer(self):
        filename = "mazes\\maze" + str(self.num) + ".png"
        
        img = cv2.imread(filename)
        ##RGBת�Ҷ�ͼ
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ##��ֵ��
        binary_img = cv2.threshold(gray_img, 1, 255, cv2.THRESH_BINARY_INV)
        ##�ҳ��߽�
        contours = cv2.findContours(binary_img[1], cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        h,w,d = img.shape
        path = np.zeros((h ,w), dtype = np.uint8)

        ##�����߽�
        cv2.drawContours(path, contours[0], 0, (255,255,255), -1)

        ##�趨һ�������
        kernel = np.ones((25,25), dtype = np.uint8)

        ##���Ͳ���
        dilate = cv2.dilate(path,kernel)
        ##�����ͺ���ٽ�����ʴ
        erosion = cv2.erode(dilate, kernel)
        ##ȡ���ͺ���ʴ�ľ��Բ�ֵ�����ó��Թ��Ľ�
        path_diff = cv2.absdiff(dilate, erosion)

        return path_diff
