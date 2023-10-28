import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

width = GetSystemMetrics(0)
heigth = GetSystemMetrics(1)
dim =(width,heigth)


f = cv2.VideoWriter_fourcc(*"XVID")

output = cv2.VideoWriter("test.mp4",f,24.0,dim)

now_start_time=time.time()
dur = 20
end_time =  now_start_time + dur
while True:
    image =pyautogui.screenshot()
    frame_1 = np.array(image)
    frame = cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB)
    output.write(frame)
    c_time =time.time()
    if c_time > end_time:
        break
output.release()
print("------ END ------")


