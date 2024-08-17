# -*- coding: utf-8 -*-
"""Facial Recognition Prerequisite.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YjmRWP14ArYG_QmE2OEsaJGC_tpPLPcu
"""

!pip install face_recognition

!pip install cmake
!pip install dlib
!pip install opencv-python

import cv2
import numpy as np
import face_recognition
from google.colab.patches import cv2_imshow

imgElon = face_recognition.load_image_file('elon1.jpg')
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('elon2.png')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

#finding faces
faceLoc = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)

#comparing the encodings and finding the distance between them
results = face_recognition.compare_faces([encodeElon],encodeTest) #true for same person, false for different persons
faceDis = face_recognition.face_distance([encodeElon],encodeTest) #higher the value, more dissimilar the two faces
print(results,faceDis)
cv2.putText(imgTest,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)


cv2_imshow(imgElon)
cv2_imshow(imgTest)
#cv2.waitKey(0)