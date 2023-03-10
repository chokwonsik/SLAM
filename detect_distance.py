import cv2
import pyrealsense2
from realsense_depth import *

# Initialize Camera Intel Realsense
dc = DepthCamera()

# ret, depth_frame, color_frame = dc.get_frame()
count = 0

while True:
    ret, depth_frame, color_frame = dc.get_frame()
    cv2.imshow("depth_frame", depth_frame)
    cv2.imwrite("dataset/depth/" + str(count) + ".png", depth_frame)
    
    cv2.imshow("color_frame", color_frame)
    cv2.imwrite("dataset/rgb/" + str(count) + ".png", color_frame)
    
    count += 1
    cv2.waitKey(500)

cv2.destroyAllWindow()

