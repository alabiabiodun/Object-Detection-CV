# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 21:55:56 2022

@author: Alabi Abiodun
"""
import cv2

img = cv2.imread('shapes.png')


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5,5),0)
imgCanny = cv2.Canny(imgBlur, 50,50)


contours,hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
imgContour = img.copy()

for cnt in contours:
    area = cv2.contourArea(cnt)
    
    if area > 500:
        contourImage = cv2.drawContours(imgContour, cnt, -1, (255,0,0),2)
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt,0.02*peri, True)
        objectCorner = len(approx)
        
        
        x,y,w,h = cv2.boundingRect(approx)
        
        
        if objectCorner == 3:
            objectType = "Tri"
            
        elif objectCorner == 4:
            objectType = "Square"
            
        elif objectCorner == 5:
            objectType = "Pent"
            
        elif objectCorner == 6:
            objectType = "Hex"
            
        elif objectCorner == 7:
            objectType = "Hep"
            
        elif objectCorner == 8:
            objectType = "Oct"
            
        else:
            objectType = "None"
            
        cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(imgContour, objectType, (x+(w//2)-10,y+(h//2)-10), 
                    cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255), 1)
        


cv2.imshow('Original Image', img)
cv2.imshow('Gray Image',imgGray)
cv2.imshow('Blur Image', imgBlur)
cv2.imshow('Edge Detection', imgCanny)
cv2.imshow('Contour Image', contourImage)
#cv2.imshow('Rect. Image', rect)



cv2.waitKey(0)

cv2.destroyAllWindows()