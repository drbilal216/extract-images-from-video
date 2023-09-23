#!pip install opencv-contrib-python

# create folder to save frames in
import os
newpath = r'C:\Users\ESHOP\Desktop\Task\1.Make program to extract images from video\Video to Images' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

# Function to save frames from video
import cv2
cam = cv2.VideoCapture("video.mp4")
currentframe = 0

while(True):
    ret,frame = cam.read()
    if ret:
        name = 'Video to Images\Frame(' + str(currentframe) + ').jpg'
        cv2.imwrite(name, frame)
        currentframe += 1
    else:
        break
        
cam.release()
cv2.destroyAllWindows()