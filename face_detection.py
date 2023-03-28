# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 11:28:51 2023

@author: merci
"""

import face_recognition
import cv2
image_to_detect=cv2.imread("C:\\Users\\merci\\Pictures\\20130713_111013.jpg")
cv2.imshow("test",image_to_detect)
all_face_locations=face_recognition.face_locations(image_to_detect,model='hog')
print(all_face_locations)
print("There are {} number of faces".format(len(all_face_locations)))
print(all_face_locations)
for index,current_face_locations in enumerate(all_face_locations):
    top,right,bottom,left=current_face_locations
    print("Face {} is found at top:{} right:{} bottom:{} left:{}".format(index+1,top,right,bottom,left))
    current_face_image=image_to_detect[top:bottom,left:right]
    #cv2.rectangle(image_to_detect,(left,top),(right,bottom),(0,0,255),2)
    cv2.imshow("Face No."+str(index+1),current_face_image)