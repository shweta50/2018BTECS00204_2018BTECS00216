import cv2
import numpy as np
import math

a=0;  #variable to count number of lines
img = cv2.imread('lines.png')
ret,img = cv2.threshold(img,180,255,0)
element = cv2.getStructuringElement(cv2.MORPH_CROSS,(6,6))
eroded = cv2.erode(img,element)
dilate = cv2.dilate(eroded, element)
skeleton = cv2.subtract(img, dilate)
gray = cv2.cvtColor(skeleton,cv2.COLOR_BGR2GRAY)
lines = cv2.HoughLinesP(gray, rho=1, theta=np.pi/360, threshold=8, minLineLength=1, maxLineGap=20)
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,255))
        a=a+1      #for each line count will increment by 1
        
cv2.imshow("lines", img)  #iamge showing lines
print("No. of lines in image....",a)

#Filling gaps in lines#
image = cv2.imread("lines.png") 
kernel = np.ones((5,2),np.uint8) ##define kernal value
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #grayscale
dilate = cv2.dilate(gray,kernel,iterations = 1)
dilate1 = cv2.morphologyEx(dilate, cv2.MORPH_OPEN, kernel) #Canny
canny = cv2.Canny(dilate1,160,160,3)
dilate = cv2.dilate(canny,kernel,iterations = 2)
#Gaussian Blurring
blur = cv2.GaussianBlur(dilate,(5,5),0)
erode = cv2.dilate(blur,kernel,iterations = 1)
blur = cv2.GaussianBlur(erode,(5,5),1)
blur = cv2.morphologyEx(blur, cv2.MORPH_CLOSE, kernel)
ret, thresh = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)
blur = cv2.GaussianBlur(thresh,(5,5),1)
ret1, thresh1 = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)
opening = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel)
cv2.imwrite('opening.jpg', opening)
contours, hierarchy = cv2.findContours(opening,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
filled=cv2.imread('opening.jpg')
thinned = cv2.ximgproc.thinning(cv2.cvtColor(filled, cv2.COLOR_RGB2GRAY))
cv2.imshow("gap-filled",thinned)
           
