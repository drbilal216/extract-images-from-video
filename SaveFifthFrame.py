#!pip install opencv-contrib-python

# create folder to save frames in
import os
newpath = r'C:\Stuff\Stydy\Work\Task\1.Make program to extract images from video\Video to Images' 
if not os.path.exists(newpath):
    os.makedirs(newpath)

# Function to save 5th frames from video
import cv2
cam = cv2.VideoCapture("test.mp4")
currentframe = 0
count = 0

while(True):
    ret,frame = cam.read()
    if ret:
        name = 'Video to Images\Frame(' + str(currentframe) + ').jpg'
        cv2.imwrite(name, frame)
        currentframe += 1
        count += 30 # How many frames to add
        cam.set(cv2.CAP_PROP_POS_FRAMES, count) # Get current frames and add extra frames
    else:
        break
        
cam.release()
cv2.destroyAllWindows()