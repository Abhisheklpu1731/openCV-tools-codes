import numpy as np
import cv2

cap = cv2.VideoCapture(0) # used to take webcam and here (0) means device number (in case you have multiple devices)
                            #you  can alse add any video or media file my putting path in instead of (0) example("/path")
while True:
    ret,frame = cap.read() #this will just start reading the frame from your capturing device
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#its a custom made function to chnage frame color to gray
    
    cv2.imshow('frame', frame)#this will make frame with name "frame"
    cv2.imshow('gray', gray)#for showing gray color frame
    
    if cv2.waitKey(1) == ord('q'): #this is to break the while loop with pressing "q"
        break
cap.release()#you must have to relese devise after program close
cv2.destroyAllWindows()#to close all fram windows
